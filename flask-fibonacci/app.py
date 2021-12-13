from flask import Flask, request, jsonify, render_template
import time as t
from fibo import Fibo

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/fibo", methods=['GET'])
def get_fibo():

    fibo_num = request.args.get('num')
    fibo_num = int(fibo_num)
    print(fibo_num)
    started_time = t.time()

    for i in Fibo.func_fibo(fibo_num):
        pass

    finished_time = t.time()
    return_time = finished_time - started_time
    print(f"Return Time = {return_time}")

    return_time = str(return_time)
    returning = "Return Time: " + return_time
    return returning

@app.route("/fibo", methods=['POST'])
def post_fibo():
    
    fibo_num = request.form['num']
    fibo_num = int(fibo_num)
    print(fibo_num)
    started_time = t.time()

    for i in Fibo.generator_fibo(fibo_num):
        pass

    finished_time = t.time()
    return_time = finished_time - started_time
    print(f"Return Time = {return_time}")

    return_time = str(return_time)
    returning = "Return Time: " + return_time
    return returning

if __name__ == '__main__':
    app.run(debug=True)
