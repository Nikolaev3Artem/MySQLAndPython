import sqlite3
class DB:
    def __init__(self):
        pass


    def create_database(self):
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS coin_info(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            AUTHOR TEXT,
            MAIN_PRICE FLOAT,
            DISCOUNT_PRICE FLOAT,
            DISCOUNT INT,
            PHOTO BLOB
            );
            """)

    def create_table(self):
        pass

    def add(self):
        pass
    
    def delete(self):
        pass

    def search(self):
        pass

    def all_database(self):
        pass