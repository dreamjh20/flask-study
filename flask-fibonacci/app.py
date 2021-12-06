from flask import Flask, request, jsonify, render_template
import time as t
from fibo import Fibo

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('')

@app.route("/fibo", methods=['GET'])
def get_fibo():
    return "function"

@app.route("/fibo", methods=['POST'])
def post_fibo():
    return "generator"

if __name__ == '__main__':
    app.run()
