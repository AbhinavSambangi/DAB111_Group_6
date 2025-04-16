from flask import Flask, render_template, g
import sqlite3
import os

app = Flask(__name__)

# Automatically get the absolute path to the 'database/nft.db' file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, '..', 'database', 'nft.db')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nft_names')
def nft_names():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT Collections FROM data")
    collections = cursor.fetchall()
    return render_template('nft_names.html', collections=collections)

@app.route('/nft_data')
def nft_data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT Collections, Sales, Buyers, Owners, Transactions FROM data")
    data = cursor.fetchall()
    return render_template('nft_data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
