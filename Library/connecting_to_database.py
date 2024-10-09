import sqlite3
from datetime import date


def conecting():
    connect = sqlite3.connect("Library.db")
    cursor = connect.cursor()
    return cursor , connect

def get_data(cursor):
    data = []
    target_date  = date(2021, 11, 3).isoformat()
    cursor.execute(f"""
    SELECT * FROM books WHERE return_at <= ?
                   """, (target_date,) )
    for id, email, name, book_title, return_at  in cursor.fetchall():
        data.append((id, email, name, book_title, return_at))
    return data
