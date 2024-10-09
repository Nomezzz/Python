"""
    This module contains operations on the database, add and delete books.
"""
from validators import is_valid_date, is_valid_emails




def add_data(cursor):
    """
    Add books to the database
    
    Args:
        cursor: Database cursor object.
    
    Returns:
        None
    """
    while True:
        email = input("Podaj email: ")
        if not is_valid_emails(email):
            print('Podaj poprawny email')
            continue

        name = input("Podaj imię: ")
        if not name:
            print('Podaj imię')
            continue

        book_title = input("Podaj tytuł książki: ")
        if not book_title:
            print('Podaj nazwę książki')
            continue

        return_at = input("Podaj datę zwrotu (YYYY.MM.DD): ")
        if not is_valid_date(return_at):
            print('Niepoprawny format daty.')
            continue

        # Dodanie książki do bazy danych
        cursor.execute("""
            INSERT INTO books (email, name, book_title, return_at)
            VALUES (?, ?, ?, ?)""", (email, name, book_title, return_at))

        print(f'Książka o tytule {book_title} została dodana.')
        break






def delete_data(cursor):
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
    book_id = input('Podaj nr ksiązki którą chcesz usunąć: ')
    cursor.execute("""
                    DELETE FROM books WHERE id = ?
                        """, (book_id))
    print(f'Książka o nr id {book_id} została usunięta  ')
