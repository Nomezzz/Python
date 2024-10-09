"""_summary_

    Args:
        create_database (_type_): _description_
    """
import sqlite3
import pytest
from connecting_to_database import get_data




@pytest.fixture
def create_test_database():
    """_summary_

    Args:
        create_database (_type_): _description_
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
    """_summary_

    Args:
        create_database (_type_): _description_
    """
    cursor = create_test_database
    data = get_data(cursor)
    assert data == [(1, 'alinka@test.email', 'Alinka', 'Potop', '2020-11-02'),
                    (2, 'adam@test.email', 'Adam', 'Ogniem i Mieczem', '2021-11-03'),
                    (3, 'kacper@test.email', 'Kacper', 'Pan Tadeusz', '2019-10-18')]

def test_add_data(create_test_database):
    """_summary_

    Args:
        create_database (_type_): _description_
    """
    cursor = create_test_database
    new_book = (5, 'ewa@test.email', 'Ewa', 'Krzyżacy', '2024-01-15')
    cursor.execute('INSERT INTO books VALUES (?, ?, ?, ?, ?)', new_book)
    cursor.execute('SELECT * FROM books WHERE id=?', (5,))
    data = cursor.fetchone()
    assert data == new_book

def test_delete_data(create_test_database):
    """_summary_

    Args:
        create_database (_type_): _description_
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
