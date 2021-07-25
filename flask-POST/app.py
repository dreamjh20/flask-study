from flask import Flask, render_template, request
import sqlite3
import datetime as dt

app = Flask(__name__)



@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/post",methods=['POST'])
def post():
	value = request.form['input']
	msg = "%s 어서 와~" %value
	print(value)
	now = dt.datetime.now()
	nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
	conn = sqlite3.connect('namedb.db', isolation_level=None)
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, regdate TEXT)")
	cur.execute("INSERT INTO users VALUES(?, ?)", (value, nowDatetime,))

	return render_template('welcome.html', value = msg)

if __name__ == "__main__":
		app.run(host='192.168.137.241')