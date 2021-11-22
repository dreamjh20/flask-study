from flask import Flask, request, jsonify
from flask_jwt_extended import *

app = Flask(__name__) #Flask에서 인스턴스 생성

app.config.update(  #Key를 환경 변수에 등록
    DEBUG = True,
    JWT_SECRET_KEY = "Moontong"
)

#임시 admin 계정 생성
admin_id = "admin"
admin_pw = "1234"

jwt = JWTManager(app) #jwt을 flask 앱에 등록

@app.route("/")
def jwt_tuto():
    return "<h1>MoonTong!</h1>"

@app.route("/login", methods=['POST'])
def login_func():
    get_data = request.get_json()
    user_id = get_data['id']
    user_pw = get_data['pw']
    #json form 에서 id와 password 파싱

    if (admin_id == user_id and admin_pw == user_pw):
        return jsonify(
            result = "SUCCESS",
            access_token = create_access_token(identity=user_id, expires_delta=False)  #create_access_tocken 으로 토큰 반환    identity는 고유 식별자, expires_delta는 토큰 만료일자 False는 무기한
        )

    else: 
        return jsonify(
			result = "Failure"
	    )

if __name__ == '__main__':
	app.run(port = 5000, debug = True)