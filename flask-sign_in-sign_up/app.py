from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def main_Page():
    print("MAIN")
    return render_template('home.html')

@app.route('/signin')
def sign_in_Page():
    return render_template('sign_in_page.html')

@app.route('/signup')
def sign_up_Page():
    return render_template('sign_up_page.html')

if __name__ == "__main__":
    app.run()