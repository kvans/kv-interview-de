from datetime import datetime

def clean_transaction_data(json_data, default_date="2000-01-01T00:00:00"):
    """
    Cleans transaction data by:
    - Removing records without a 'user_id'.
    - Converting 'amount' to float safely.
    - Converting 'timestamp' to datetime, replacing invalid dates with a default value.

    :param json_data: List of transaction records (JSON format).
    :param default_date: Default date string for invalid timestamps.
    :return: List of cleaned transaction records.
    """
    cleaned_data = []
    default_datetime = datetime.fromisoformat(default_date)  # Default date as datetime object
    skipped_rows = 0

    for row in json_data:
        # Skip rows where 'user_id' is missing
        if row.get("user_id") is None:

        # Convert 'amount' to float safely
        try:
        except ValueError:

        # Convert timestamp to datetime, replacing invalid values with default date
        try:
        except (ValueError, TypeError):

        # Add cleaned record to output list

    print(f"Processed {len(cleaned_data)} valid records, skipped {skipped_rows} invalid row(s).")
    return cleaned_data

json_data = [
    {"transaction_id": "TXN12345", "user_id": "USR001", "amount": "100.50", "currency": "USD", "timestamp": "2025-01-30T14:30:00", "status": "completed"},
    {"transaction_id": "TXN12346", "user_id": "USR002", "amount": 50.25, "currency": "EUR", "timestamp": "2025-01-30T15:00:00", "status": "pending"},
    {"transaction_id": "TXN12347", "user_id": "USR003", "amount": None, "currency": "USD", "timestamp": "INVALID_DATE", "status": "failed"},
    {"transaction_id": "TXN12348", "user_id": "USR004", "amount": "200abc", "currency": "GBP", "timestamp": "2025-01-30T17:45:00", "status": "completed"},
    {"transaction_id": "TXN12349", "user_id": None, "amount": 75.00, "currency": "USD", "timestamp": "2025-01-30T18:10:00", "status": "completed"}
]

cleaned_data = clean_transaction_data(json_data)
print(cleaned_data)