# importing sqlite to work with database
import sqlite3

# class for all database queries working for
class DB:
    # when database inited we have this code
    def __init__(self):
        # adding connection to database
        self.connection = sqlite3.connect('books.db', check_same_thread=False)
        # our cursor
        self.cursor = self.connection.cursor()
        # data shortcods for sqlite
        self.data_insert_request = """ INSERT INTO books(NAME, AUTHOR, GENRE,MAIN_PRICE, DISCOUNT_PRICE, DISCOUNT, PRICE_CURRENCY, PHOTO) VALUES(?,?,?,?,?,?,?,?)"""
        self.first_id_request = """ SELECT * FROM books WHERE ID = 1 """
        self.all_db_request = """SELECT * FROM books"""
        self.find_for_name = """ SELECT * FROM books WHERE NAME = ? """

    # creating our table
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            AUTHOR TEXT,
            GENRE TEXT,
            MAIN_PRICE TEXT,
            DISCOUNT_PRICE TEXT,
            DISCOUNT TEXT,
            PRICE_CURRENCY TEXT,
            PHOTO TEXT
            );
            """)

    # inserting data in table, used from parser
    def add(self,data):
        self.cursor.execute(self.data_insert_request,data)
        self.connection.commit()

    # returning all database to work with, used in main program to display it
    def return_all_database(self):
        self.cursor.execute(self.all_db_request)
        records = self.cursor.fetchall()
        all_db = []
        
        for row in records:
            all_db.append(row)
        return(all_db)

    # returning our first book from database to output it for our user
    def first_book(self):
        self.cursor.execute(self.first_id_request)
        rows = self.cursor.fetchall()
        book_list = []

        for row in rows:
            book_list.append(row)
        
        return book_list

    def find_book_for_name(self,name):
        self.cursor.execute(self.find_for_name , (name,))
        rows = self.cursor.fetchall()
        book_for_name_list = []

        for row in rows:
            book_for_name_list.append(row)
        
        return book_for_name_list
        