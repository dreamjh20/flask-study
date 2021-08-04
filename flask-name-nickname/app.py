from os import name
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def Input():
	return render_template('index.html')

@app.route("/welcome", methods=['POST'])
def Post():
    name = request.form['name']
    nickname = request.form['nickname']
    print(name, nickname)
    conn = sqlite3.connect("user.db", isolation_level=None)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (name text, nickname text)")
    cur.execute("INSERT INTO users VALUES(?, ?)", (name, nickname))
    cur.execute("SELECT * FROM users")
    # for row in cur.fetchall():
    #     print(row)
    nickname_list = cur.fetchall()
    print(nickname_list)
    return render_template('welcome.html', value1 = name)

@app.route("/result", methods=['POST'])
def Result():
    print


if __name__ == "__main__":
    app.run()