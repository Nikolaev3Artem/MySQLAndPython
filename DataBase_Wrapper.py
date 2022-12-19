import sqlite3
class DB:
    def __init__(self):
        self.connection = sqlite3.connect('books.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.data_insert_request = """ INSERT INTO books(NAME, AUTHOR, MAIN_PRICE, DISCOUNT_PRICE, DISCOUNT, PRICE_CURRENCY, PHOTO) VALUES(?,?,?,?,?,?,?)"""
        self.first_id_request = """ SELECT * FROM books WHERE ID = 2 """
        self.all_db_request = """SELECT * FROM books"""

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            AUTHOR TEXT,
            MAIN_PRICE TEXT,
            DISCOUNT_PRICE TEXT,
            DISCOUNT TEXT,
            PRICE_CURRENCY TEXT,
            PHOTO TEXT
            );
            """)

    def add(self,data):
        self.cursor.execute(self.data_insert_request,data)
        self.connection.commit()

    def return_all_database(self):
        self.cursor.execute(self.all_db_request)
        records = self.cursor.fetchall()
        all_db = []
        
        for row in records:
            all_db.append(row)
        return(all_db)

    def search(self):
        pass

    def show_all_database(self):
        pass

    def first_book(self):
        self.cursor.execute(self.first_id_request)
        rows = self.cursor.fetchall()
        book_list = []

        for row in rows:
            book_list.append(row)
        
        return book_list

        