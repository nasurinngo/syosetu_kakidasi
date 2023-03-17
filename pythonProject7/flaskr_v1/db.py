import sqlite3

DATABASE = 'database.db'

def create_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE Quiz(問題ID INTEGER, 書き出し VARCHAR(100)) IF NOT EXISTS books (title, price, arrival_day)")
    con.close()