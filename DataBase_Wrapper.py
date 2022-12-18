import sqlite3
class DB:
    def __init__(self):
        self.connection = sqlite3.connect('books.db')
        self.cursor = self.connection.cursor()


    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            AUTHOR TEXT,
            MAIN_PRICE FLOAT,
            DISCOUNT_PRICE FLOAT,
            DISCOUNT INT,
            PRICE_CURRENCY TEXT, 
            PHOTO BLOB
            );
            """)

    def add(self):
        self.cursor.execute(""" INSERT INTO """)
    
    def delete(self):
        pass

    def search(self):
        pass

    def all_database(self):
        pass