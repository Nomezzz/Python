"""
This module provides functionality for managing borrowed books,
including sending email reminders to borrowers.
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
from connecting_to_database import conecting, get_data


def get_borrowers():
    """
    Retrieves a list of borrowers from the database.
    
    Returns:
        list: A list of tuples containing borrower information,
          where each tuple has the following elements:
            - receiver (str): The email address of the borrower.
            - name (str): The name of the borrower.
            - book_title (str): The title of the borrowed book.
            - return_at (str): The date the book is due to be returned.
    """
    cursor = conecting()
    data = get_data(cursor)
    return data

def send_email(borrowers_list):
    """
    Sends email reminders to borrowers about returning books.
    
    Args:
        borrowers_list (list): A list of tuples containing borrower information,
          where each tuple has the following elements:
            - receiver (str): The email address of the borrower.
            - name (str): The name of the borrower.
            - book_title (str): The title of the borrowed book.
            - return_at (str): The date the book is due to be returned.
    
    Returns:
        None
    """
    for borrower in borrowers_list:
        receiver = borrower[1]
        name = borrower[2]
        book_title = borrower[3]
        return_at = borrower[4]

        message_template = Template("""Cześć $name! Czy masz jeszcze moją książkę?
                                     Chodzi mi o '$book_title'.
        Pamiętaj proszę, że umawialiśmy się, że oddasz mi ją $return_at. 
        Będę bardzo wdzięczny, jeśli oddasz mi ją w ustalonym terminie lub szybciej!""")
        text = message_template.substitute(name=name, book_title=book_title, return_at=return_at)

        sender = "Library in NY <mailtrap@demomailtrap.com>"

        message = MIMEMultipart()
        message['Subject'] = "Przypomnienie o zwrocie książki"
        message['From'] = sender
        message['To'] = receiver
        message.attach(MIMEText(text, 'plain', 'utf-8'))
        with smtplib.SMTP("bulk.smtp.mailtrap.io", 587) as server:
            server.starttls()
            server.login("api", "97f0efc5f83aa470f6faed0640c71010")
            server.sendmail(sender, receiver, message.as_string())
            print(f"E-mail wysłany do: {receiver, name}")

if __name__ == "__main__":
    borrowers = get_borrowers()
    send_email(borrowers)
