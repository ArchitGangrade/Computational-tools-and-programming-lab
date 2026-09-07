import sqlite3
import os


class LibraryModel:

    def __init__(self):
        # Create database folder if it does not exist
        os.makedirs("database", exist_ok=True)

        self.database = "database/library.db"

        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.database)

    def create_tables(self):
        connection = self.connect()
        cursor = connection.cursor()

        # Books table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)

        # Issued books table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS issued_books (
                issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                student_name TEXT NOT NULL,
                issue_date TEXT NOT NULL,
                FOREIGN KEY (book_id) REFERENCES books(book_id)
            )
        """)

        connection.commit()
        connection.close()

    # ---------------- ADD BOOK ----------------

    def add_book(self, book_id, title, author, quantity):
        try:
            connection = self.connect()
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO books (book_id, title, author, quantity)
                VALUES (?, ?, ?, ?)
            """, (book_id, title, author, quantity))

            connection.commit()
            connection.close()

            return True, "Book added successfully."

        except sqlite3.IntegrityError:
            return False, "Book ID already exists."

        except Exception as error:
            return False, str(error)

    # ---------------- GET BOOK ----------------

    def get_book(self, book_id):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM books WHERE book_id = ?
        """, (book_id,))

        book = cursor.fetchone()

        connection.close()

        return book

    # ---------------- ISSUE BOOK ----------------

    def issue_book(self, book_id, student_name, issue_date):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT quantity FROM books
            WHERE book_id = ?
        """, (book_id,))

        book = cursor.fetchone()

        if book is None:
            connection.close()
            return False, "Book not found."

        if book[0] <= 0:
            connection.close()
            return False, "Book is not available."

        cursor.execute("""
            INSERT INTO issued_books
            (book_id, student_name, issue_date)
            VALUES (?, ?, ?)
        """, (book_id, student_name, issue_date))

        cursor.execute("""
            UPDATE books
            SET quantity = quantity - 1
            WHERE book_id = ?
        """, (book_id,))

        connection.commit()
        connection.close()

        return True, "Book issued successfully."

    # ---------------- RETURN BOOK ----------------

    def return_book(self, book_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT issue_id
            FROM issued_books
            WHERE book_id = ?
            ORDER BY issue_id
            LIMIT 1
        """, (book_id,))

        issued_book = cursor.fetchone()

        if issued_book is None:
            connection.close()
            return False, "This book is not currently issued."

        issue_id = issued_book[0]

        cursor.execute("""
            DELETE FROM issued_books
            WHERE issue_id = ?
        """, (issue_id,))

        cursor.execute("""
            UPDATE books
            SET quantity = quantity + 1
            WHERE book_id = ?
        """, (book_id,))

        connection.commit()
        connection.close()

        return True, "Book returned successfully."

    # ---------------- SEARCH BOOK ----------------

    def search_books(self, search_text):

        connection = self.connect()
        cursor = connection.cursor()

        search_text = "%" + search_text + "%"

        cursor.execute("""
            SELECT book_id, title, author, quantity
            FROM books
            WHERE CAST(book_id AS TEXT) LIKE ?
               OR title LIKE ?
               OR author LIKE ?
        """, (search_text, search_text, search_text))

        books = cursor.fetchall()

        connection.close()

        return books

    # ---------------- GET ALL BOOKS ----------------

    def get_all_books(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT book_id, title, author, quantity
            FROM books
            ORDER BY book_id
        """)

        books = cursor.fetchall()

        connection.close()

        return books

    # ---------------- GET ISSUED BOOKS ----------------

    def get_issued_books(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                issued_books.issue_id,
                issued_books.book_id,
                books.title,
                issued_books.student_name,
                issued_books.issue_date
            FROM issued_books
            JOIN books
            ON issued_books.book_id = books.book_id
            ORDER BY issued_books.issue_id
        """)

        records = cursor.fetchall()

        connection.close()

        return records

