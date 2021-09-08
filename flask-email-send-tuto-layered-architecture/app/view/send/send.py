from flask import request
from flask_restful import Resource
from app.util.email_send import send_email

class Send(Resource):
    def post(self):
        rec_name = request.form['Receiver']
        title = request.form['Head']
        message = request.form['Body']
        print(rec_name)
        print(title)
        print(message)
        
        print('1111')
        print('2222')
        print(rec_name, title, message)
        print('3333')
        send_email()
        print('4444')
        return 'Sent'