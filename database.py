import os
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
    host=os.getenv('MYSQL_HOST', 'localhost'),
    port=os.getenv('MYSQL_PORT', 3306),
    user=os.getenv('MYSQL_USER', 'root'),
    password=os.getenv('MYSQL_PASSWORD', 'Mosim1991m2'),
    database=os.getenv('MYSQL_DATABASE', 'library_db')
)

def add_book(title, author, year, genre):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO books (title,author,publication_year,genre) VALUES (%s,%s,%s,%s)"
    values = (title, author, year, genre)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def get_all_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM books"
    cursor.execute(query)
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books


def search_books(keyword):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM books WHERE title LIKE %s OR genre LIKE %s"
    cursor.execute(query, (f'%{keyword}%', f'%{keyword}%'))
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books


def get_book_by_id(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM books WHERE id= %s"
    cursor.execute(query, (book_id,))
    book = cursor.fetchall()
    cursor.close()
    conn.close()
    return book


def update_book(book_id, title, author, year, genre):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE books SET title =%s, author=%s, publication_year=%s, genre=%s WHERE id=%s"
    cursor.execute(query, (title, author, year, genre, book_id))
    conn.commit()
    cursor.close()


def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM books WHERE id=%s"
    cursor.execute(query, (book_id,))
    conn.commit()
    cursor.close()
