from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("user.db", isolation_level=None)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id text, password text, email text)")

@app.route('/')
def home_page():
    print("HOME")
    return render_template('home.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/result', methods=['POST'])
def main_page():
    conn = sqlite3.connect("user.db", isolation_level=None)
    cur = conn.cursor()
    
    check = request.form['check']

    print(check)

    #Login
    if check == 'login':
        Id=request.form['id']
        Pw = request.form['pw']
        print(Id, Pw)

        PW = cur.execute("SELECT password FROM users WHERE users.id ==?", (Id, ))
        PW = cur.fetchone()
        PW = str(PW)
        PW = PW[2:-3]
        print(PW)
        if Pw == PW:
            print("SUCCEED")
        else:
            print("FAIL")

    #Signup
    else:
        Id=request.form['id']
        Pw = request.form['pw']
        print(Id, Pw)
        #Exist
        
        #Non Exist
    return render_template('result.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()