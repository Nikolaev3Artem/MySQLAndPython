import sqlite3
class DB:
    def __init__(self):
        self.connection = sqlite3.connect('books.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.data_insert = """ INSERT INTO books(NAME, AUTHOR, MAIN_PRICE, DISCOUNT_PRICE, DISCOUNT, PRICE_CURRENCY) VALUES(?,?,?,?,?,?)"""
        self.first_id = """ SELECT * FROM books WHERE ID = 1 """

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            AUTHOR TEXT,
            MAIN_PRICE TEXT,
            DISCOUNT_PRICE TEXT,
            DISCOUNT TEXT,
            PRICE_CURRENCY TEXT
            );
            """)

    def add(self,data):
        self.cursor.execute(self.data_insert,data)
        self.connection.commit()

    def delete(self):
        pass

    def search(self):
        pass

    def show_all_database(self):
        pass

    def first_book(self):
        self.cursor.execute(self.first_id)
        rows = self.cursor.fetchall()
        book_list = []

        for row in rows:
            book_list.append(row)
        
        return book_list

        