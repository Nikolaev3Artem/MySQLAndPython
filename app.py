# importing all that we need to main program
from flask import Flask, render_template
from DataBase_Wrapper import DB

# initializing flask and dabatase
db = DB()
app = Flask(__name__)

# creating table if need
db.create_table()

# making rout to main page where we will send and receive data
@app.route("/", methods = ['GET','POST'])
def hello_world():
    book = db.first_book()
    books = db.return_all_database()
    books.reverse()

    book_name = book[0][1]
    book_author = book[0][2]
    book_price = book[0][3]
    book_currency_price = book[0][6]
    book_img = book[0][7]
    if book[0][4] or book[0][5] == "None":
        book_discount_price = ""
        book_discount_procent = ""
        book_currency_discount = ""
    else:
        book_discount_price = book[0][4]
        book_discount_procent = book[0][5]
        book_currency_discount = book[0][6]
    
    return render_template("index.html",
    book_discount_procent = book_discount_procent,
    book_name = book_name,
    book_author = book_author,
    book_price = book_price,
    book_discount_price = book_discount_price,
    book_currency_price = book_currency_price,
    book_currency_discount = book_currency_discount,
    book_img = book_img,
    books = books[0:10]
    )

# running our flask app
if __name__ == '__main__':
    app.run(debug=True)