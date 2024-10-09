"""_summary_

    Args:
        create_database (_type_): _description_
    """
import sqlite3
import pytest
from connecting_to_database import get_data




@pytest.fixture
def create_test_database():
    """Creates a temporary in-memory test database for testing purposes.

    This fixture sets up an SQLite database in memory, creates a table for
    storing book data, and populates it with sample data. This allows for
    isolated tests that do not affect any real database.

    Returns:
        sqlite3.Cursor: A cursor object for the in-memory database.
    """
    connect = sqlite3.connect(":memory:")
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE books
        (id INTIGER, email TEXT, name TEXT, book_title TEXT, return_at DATE)
                    """)
    sample_date =[
	(1, 'alinka@test.email', 'Alinka', 'Potop', "2020-11-02"),
	(2, 'adam@test.email', 'Adam', 'Ogniem i Mieczem', "2021-11-03"),
	(3, 'kacper@test.email', 'Kacper', 'Pan Tadeusz', "2019-10-18"),
	(4, 'albert@test.mail', 'Albert', 'W Pustyni i w puszczy', "2035-11-12")
    ]
    cursor.executemany('INSERT INTO books VALUES (?, ?, ?, ?, ?)', sample_date)
    return cursor


def test_get_data(create_test_database):
    """Tests the get_data() function for retrieving book records.

    This test checks whether the get_data() function returns the correct
    list of book records from the in-memory database.

    Args:
        create_test_database (sqlite3.Cursor): A cursor for the test database.

    Raises:
        AssertionError: If the retrieved data does not match expected values.
    """
    cursor = create_test_database
    data = get_data(cursor)
    assert data == [(1, 'alinka@test.email', 'Alinka', 'Potop', '2020-11-02'),
                    (2, 'adam@test.email', 'Adam', 'Ogniem i Mieczem', '2021-11-03'),
                    (3, 'kacper@test.email', 'Kacper', 'Pan Tadeusz', '2019-10-18')]

def test_add_data(create_test_database):
    """Tests the addition of a new book record to the database.

    This test verifies that a new book record can be added to the
    in-memory database and checks if the data is correctly stored.

    Args:
        create_test_database (sqlite3.Cursor): A cursor for the test database.

    Raises:
        AssertionError: If the newly added record does not match the input data.
    """
    cursor = create_test_database
    new_book = (5, 'ewa@test.email', 'Ewa', 'Krzyżacy', '2024-01-15')
    cursor.execute('INSERT INTO books VALUES (?, ?, ?, ?, ?)', new_book)
    cursor.execute('SELECT * FROM books WHERE id=?', (5,))
    data = cursor.fetchone()
    assert data == new_book

def test_delete_data(create_test_database):
    """Tests the deletion of a book record from the database.

    This test verifies that a book record can be deleted from the
    in-memory database and checks if the remaining records are correct.

    Args:
        create_test_database (sqlite3.Cursor): A cursor for the test database.

    Raises:
        AssertionError: If the remaining records do not match expected values after deletion.
    """
    cursor = create_test_database
    cursor.execute('DELETE FROM books WHERE id=?', (5,))
    cursor.execute('SELECT * FROM books')
    data = cursor.fetchall()
    assert data == [
	(1, 'alinka@test.email', 'Alinka', 'Potop', "2020-11-02"),
	(2, 'adam@test.email', 'Adam', 'Ogniem i Mieczem', "2021-11-03"),
	(3, 'kacper@test.email', 'Kacper', 'Pan Tadeusz', "2019-10-18"),
	(4, 'albert@test.mail', 'Albert', 'W Pustyni i w puszczy', "2035-11-12")
    ]
