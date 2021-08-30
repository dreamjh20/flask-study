from os import name
from re import A, search
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

    name_exist = cur.execute("SELECT nickname FROM users WHERE users.name ==?", (name, ))
    name_exist = cur.fetchone()
    if name_exist == None:
        cur.execute("INSERT INTO users VALUES(?, ?)", (name, nickname))
        

    else :
        cur.execute("UPDATE users SET nickname = ? WHERE users.name == ?", (nickname, name))
        print("UPDATE")
    conn.close()
    return render_template('welcome.html', value1 = name)

@app.route("/search", methods=['POST'])
def Result():
    search_name = request.form['search_word']
    print(search_name)
    conn = sqlite3.connect("user.db", isolation_level=None)
    cur = conn.cursor()
    print("====================")
    result_nickname = cur.execute("SELECT nickname FROM users WHERE users.name ==?", (search_name, ))
    result_nickname = cur.fetchone()
    print(result_nickname)
    print(type(result_nickname))
    if result_nickname == None:
        name_nickname = "No nickname yet."
    else:
        result_nickname = str(result_nickname)
        result_nickname = result_nickname[2:-3]
        print(result_nickname)
        name_nickname = search_name + ' IS ' + result_nickname
    print("--------------------")
    conn.close()
    return render_template('search.html', value = name_nickname)

if __name__ == "__main__":
    app.run()