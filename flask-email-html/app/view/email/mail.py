from flask_restful import Resource

class SendEmail(Resource):
    def post(self):
        print("EMAIL")
        return 'email'