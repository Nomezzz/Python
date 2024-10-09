"""_summary_

    Returns:
    _type_: _description_
    """
import sqlite3
from datetime import date


def conecting():
    """  Establishes a connection to the SQLite database and returns the cursor and connection objects.

    Returns:
        tuple: A tuple containing:
            - cursor (sqlite3.Cursor): The cursor object used to execute SQL commands.
            - connect (sqlite3.Connection): The connection object for the SQLite database.
    """
    connect = sqlite3.connect("Library.db")
    cursor = connect.cursor()
    return cursor , connect

def get_data(cursor):
    """ Retrieves book data from the database where the return
      date is less than or equal to a specified target date.

    Returns:
         list: A list of tuples containing book information, where each tuple has the following elements:
            - book_id (int): The unique identifier for the book.
            - email (str): The email address of the borrower.
            - name (str): The name of the borrower.
            - book_title (str): The title of the borrowed book.
            - return_at (str): The date the book is due to be returned.
    """
    data = []
    target_date  = date(2021, 11, 3).isoformat()
    cursor.execute("""
    SELECT * FROM books WHERE return_at <= ?
                   """, (target_date,) )
    for id, email, name, book_title, return_at  in cursor.fetchall():
        data.append((id, email, name, book_title, return_at))
    return data
