from os import name
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("test.db", isolation_level=None)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, name text, nickname text)")

@app.route("/")
def Input():
	return render_template('index.html')

@app.route("/succeed", methods=['POST'])
def Post():
    name = request.form['name']
    nickname = request.form['nickname']
    print(name, nickname)

if __name__ == "__main__":
    app.run()