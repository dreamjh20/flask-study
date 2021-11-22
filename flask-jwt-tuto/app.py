from flask import Flask
from flask_jwt_extended import *

app = Flask(__name__) #Flask에서 인스턴스 생성

app.config.update(  #Key를 환경 변수에 등록
    DEBUG = True,
    JWT_SECRET_KEY = "Moontong"
)

jwt = JWTManager(app) #jwt을 flask 앱에 등록

@app.route("/")
def jwt_tuto():
    return "<h1>MoonTong!</h1>"

    
if __name__ == '__main__':
	app.run(port = 5000, debug = True)