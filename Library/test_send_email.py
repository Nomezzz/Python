"""
    This module contains a test for the `send_email` function in the `main.py` file.
"""
from unittest.mock import patch
from main import send_email

@patch('smtplib.SMTP')
def test_send_email(mock_smtp):
    """
    Tests the `send_email` function by mocking the `smtplib.SMTP` class.
    
    The test creates a mock list of borrowers and calls the `send_email`
      function with this list. It then asserts that the `smtplib.SMTP`
        class was called, verifying that the function correctly sends an email.
    """
    mock_borrowers = ["test@example.com"]
    send_email(mock_borrowers)
    mock_smtp.assert_called()
