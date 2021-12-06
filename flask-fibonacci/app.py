from flask import Flask, request, jsonify, render_template
import time as t
from fibo import Fibo

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/fibo", methods=['GET'])
def get_fibo():
    started_time = t.time()

    for i in Fibo.func_fibo(500000):
        pass

    finished_time = t.time()
    return_time = finished_time - started_time
    print(f"Return Time = {return_time}")

    return_time = str(return_time)
    return return_time

@app.route("/fibo", methods=['POST'])
def post_fibo():
    
    started_time = t.time()

    for i in Fibo.generator_fibo(500000):
        pass

    finished_time = t.time()
    return_time = finished_time - started_time
    print(f"Return Time = {return_time}")

    return_time = str(return_time)
    return return_time

if __name__ == '__main__':
    app.run()
