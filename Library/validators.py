from datetime import datetime

def is_valid_emails(email):
    return "@" in email and "." in email

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y.%m.%d")
        return True
    except ValueError:
        return False
