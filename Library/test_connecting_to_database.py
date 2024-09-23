import pytest
import sqlite3
from connecting_to_database import get_data


@pytest.fixture
def create_database():
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


def test_get_data(create_database):
    cursor = create_database
    data = get_data(cursor)
    assert data == [(1, 'alinka@test.email', 'Alinka', 'Potop', '2020-11-02'),
                    (2, 'adam@test.email', 'Adam', 'Ogniem i Mieczem', '2021-11-03'),
                    (3, 'kacper@test.email', 'Kacper', 'Pan Tadeusz', '2019-10-18')]