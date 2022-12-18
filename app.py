from flask import Flask, render_template
from DataBase_Wrapper import DB

db = DB()
app = Flask(__name__)

db.create_database()

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)