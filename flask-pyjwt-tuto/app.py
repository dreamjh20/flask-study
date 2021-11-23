#jwt 모듈 임포트
import jwt

#json form 데이터 생성
data ={
    "id": "Moon",
    "admin": True
}

#Secret Key 지정
SECRET = 'jwt_moon'

#jwt 생성   데이터와  시크릿 키를 인코딩
#type은 JWT, HS256 알고리즘으로 해싱
jwtoken = jwt.encode(data, SECRET)

print(jwtoken)