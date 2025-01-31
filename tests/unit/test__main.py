import pytest
from datetime import datetime
from src.main import clean_transaction_data  # Replace 'your_module' with the actual module name

@pytest.fixture
def sample_json_data():
    """Fixture providing sample JSON data with various edge cases."""
    return [
        {"transaction_id": "TXN12345", "user_id": "USR001", "amount": "100.50", "currency": "USD", "timestamp": "2025-01-30", "status": "completed"},
        {"transaction_id": "TXN12346", "user_id": "USR002", "amount": 50.25, "currency": "EUR", "timestamp": "2025-01-30", "status": "pending"},
        {"transaction_id": "TXN12347", "user_id": "USR003", "amount": None, "currency": "USD", "timestamp": "INVALID_DATE", "status": "failed"},
        {"transaction_id": "TXN12348", "user_id": "USR004", "amount": "200abc", "currency": "GBP", "timestamp": "2025-01-30", "status": "completed"},
        {"transaction_id": "TXN12349", "user_id": None, "amount": 75.00, "currency": "USD", "timestamp": "2025-01-30", "status": "completed"}
    ]

def test_cleaned_data_structure(sample_json_data):
    """Test if the function returns a list of cleaned transaction dictionaries."""
    cleaned_data = clean_transaction_data(sample_json_data)

    assert isinstance(cleaned_data, list), "Output should be a list"
    assert all(isinstance(record, dict) for record in cleaned_data), "Each record should be a dictionary"

def test_missing_user_id_exclusion(sample_json_data):
    """Test if records with missing 'user_id' are removed."""
    cleaned_data = clean_transaction_data(sample_json_data)
    
    # Ensure the row with missing 'user_id' is not included
    assert len(cleaned_data) == 4, "Rows with missing user_id should be excluded"

def test_amount_conversion(sample_json_data):
    """Test if 'amount' is correctly converted to a float."""
    cleaned_data = clean_transaction_data(sample_json_data)

    assert isinstance(cleaned_data[0]["amount"], float), "Amount should be a float"
    assert cleaned_data[0]["amount"] == 100.50, "Amount should retain its original float value"
    assert cleaned_data[3]["amount"] is None, "Invalid numeric values should be converted to None"

def test_invalid_timestamp_handling(sample_json_data):
    """Test if invalid timestamps are replaced with the default datetime."""
    default_datetime = datetime(2000, 1, 1, 0, 0)
    cleaned_data = clean_transaction_data(sample_json_data)

    assert isinstance(cleaned_data[0]["timestamp"], datetime), "Timestamp should be converted to datetime"
    assert cleaned_data[2]["timestamp"] == default_datetime, "Invalid timestamps should be replaced with the default date"

def test_valid_timestamp_conversion(sample_json_data):
    """Test if valid timestamps are correctly parsed into datetime objects."""
    cleaned_data = clean_transaction_data(sample_json_data)

    assert cleaned_data[0]["timestamp"] == datetime(2025, 1, 30, 0, 0), "Valid timestamps should be parsed correctly"

def test_log_output_for_skipped_rows(sample_json_data, capsys):
    """Test if the function correctly logs the number of skipped rows."""
    clean_transaction_data(sample_json_data)

    captured = capsys.readouterr()
    assert "skipped 1 invalid row(s)" in captured.out, "Function should log the number of skipped rows"
