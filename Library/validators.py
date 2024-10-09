"""
    This module contains validation functions for various input types.

Functions:
- is_valid_date(date_str: str) -> bool: Validates if the given date string is in the correct format.
- is_valid_emails(email: str) -> bool: Validates if the given email address is correctly formatted.
"""
from datetime import datetime

def is_valid_emails(email):
    """ 
    Validates if the given email address is correctly formatted.

    Args:
        email (str):The email address to validate and have @.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    return "@" in email and "." in email

def is_valid_date(date_str):
    """   
    Validates if the given date string is in the correct format (YYYY.MM.DD).

    Args:
        date_str (str): The date string to validate

    Returns:
        bool: True if the date string is valid, False otherwise.
    """
    try:
        datetime.strptime(date_str, "%Y.%m.%d")
        return True
    except ValueError:
        return False
