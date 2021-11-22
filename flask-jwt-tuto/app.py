from flask import Flask
from flask_jwt_extended import *

app = Flask(__name__) #Flask에서 인스턴스 생성

@app.route("/")
def jwt_tuto():
    return "<h1>MoonTong!</h1>"

    
if __name__ == '__main__':
	app.run(port = 5000, debug = True)