import mysql.connector
from tkinter import ttk, messagebox
class BD:
    def __init__(self):
        try:
            self.mysql_connection = mysql.connector.connect(
                host='localhost',
                user='Temp',
                password='1111')
            print("Connection to MySQL DB successful")
            self.cursor = self.mysql_connection.cursor()
        except mysql.connector.Error as error:
            print(f"The error '{error}' occurred")

    def create_database(self):
        try:
            self.cursor.execute("""CREATE schema if not exists Mediateka""")
        except mysql.connector.Error as error:
            print(f"The error '{error}' occurred")

    def add_table(self):
        try:
            create_table_query = ("""use Mediateka;
            CREATE TABLE IF NOT EXISTS films (
                    film_id             INT PRIMARY KEY AUTO_INCREMENT, 
                    film_title          VARCHAR (32), 
                    film_year           INT (10), 
                    film_genre          VARCHAR (32), 
                    film_imdb           VARCHAR (32),
                    film_poster         LONGBLOB)
                    """)
            self.cursor.execute(create_table_query)
        except mysql.connector.Error as error:
            print(f"Помилка '{error}'")


    def convertToBinaryData(self, filename):
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    def add(self, film_title, year, genre, imdb, photo):
        try:
            sql_insert_query = """    INSERT INTO mediateka.films
                                          (film_title, film_year, film_genre, film_imdb, film_poster)  VALUES (%s, %s, %s, %s, %s)"""
            tempPhoto = self.convertToBinaryData(photo)
            data_tuple = (film_title, year, genre, imdb, tempPhoto)
            self.cursor.execute(sql_insert_query, data_tuple)
            self.mysql_connection.commit()
            messagebox.showinfo('Успіх', 'Запис додано')
        except mysql.connector.Error as error:
            print(f"Помилка '{error}'")

    def show(self):
        try:
            self.cursor.execute("SELECT film_id, film_title, film_year, film_genre, film_imdb FROM mediateka.films")
            data = self.cursor.fetchall()
            return data
        except mysql.connector.Error as error:
            print(f"Помилка '{error}'")

    def writeTofile(self, data):
        filename = 'myfile.img'
        with open('myfile.img', 'wb') as f:
            f.write(data)
        return filename

    def readBlobData(self, empId):
        sql_fetch_blob_query = """SELECT * from mediateka.films where film_id = %s"""
        self.cursor.execute(sql_fetch_blob_query, (empId,))
        record = self.cursor.fetchall()
        profile1 = record[0][5]
        profile = self.writeTofile(profile1)
        return profile

    def search(self, title="", year="", genre="", imdb=""):
        try:
            if title != "":
                self.cursor.execute("SELECT * FROM mediateka.films WHERE film_title LIKE %s", ('%' + title + '%',))
            elif year != "":
                self.cursor.execute("SELECT * FROM mediateka.films WHERE film_year LIKE %s", ('%' + year + '%',))
            elif genre != "":
                self.cursor.execute("SELECT * FROM mediateka.films WHERE film_genre=%s", (genre,))
            elif imdb != "":
                self.cursor.execute("SELECT * FROM mediateka.films WHERE film_imdb LIKE %s", ('%' + imdb + '%',))
            znah = self.cursor.fetchall()
            return znah
        except mysql.connector.Error as error:
            print(f"Помилка '{error}'")

    def __del__(self):
        self.mysql_connection.close()

