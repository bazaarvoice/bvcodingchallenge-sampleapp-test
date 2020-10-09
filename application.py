from flask import Flask
from flask import render_template
from datetime import datetime
from helpers.database_helper import Database

app = Flask(__name__)
database = Database()

@app.route('/')
def homepage():
    run_database_test()
    return render_template('index.html', now=datetime.now())

def run_database_test():
    print(database.run_query("SELECT * FROM reviews"))
    return None
