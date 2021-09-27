from flask import Flask, render_template, request
from flask_mail import Mail, Message
from email.message import EmailMessage
import imghdr
import random

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mungshilcloud@gmail.com'
app.config['MAIL_PASSWORD'] = 'andtlfrnfma!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['POST'])
def send_email():
    # name = request.form['Receiver']
    name = 'ddongungga@gmail.com'
    title = 'Mungshil Cloud Email Verification'
    
    # msg = Message(title, sender='mungshilcloud@gmail.com', recipients=[name])
    msg = Message(title, sender='mungshilcloud@gmail.com', recipients=[name])
    # msg.html="""
    #             <img src="https://avatars.githubusercontent.com/u/86836065?s=40&v=4">
    #          """

    with open('ms_icon.jpg') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    # msg.html = render_template('test.html')
    # print(msg)

    msg.add_attatchment(file_data, main_type="image", sub_type=file_type, filename=file_name)

    print('111111111111111111111')
    # rand_code = random.randrange(100000, 999999)
    # rand_code = str(rand_code)
    # msg.body = rand_code
    # print(rand_code)
    print('222222222222222222222')
    mail.send(msg) 
    print('333333333333333333333')
    return 'Sent'

if __name__ == '__main__' :
    app.run()