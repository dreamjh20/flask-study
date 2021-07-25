from flask import Flask
from flask import request
 
app = Flask(__name__)
 
@app.route('/')
def user_loc():
    temp = request.args.get('name', "DEFALT: user01")
    temp1 = request.args.get('loc', "DEFAULT: 목포시")
 
    return temp + "-" + temp1

if __name__ == "__main__":
		app.run()