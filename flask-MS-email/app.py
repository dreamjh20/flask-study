from flask import Flask, render_template, request
from flask_mail import Mail, Message
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

    rand_code = random.randrange(100000, 999999)
    rand_code = str(rand_code)
    # name = request.form['Receiver']
    name = '201101kkj@dsm.hs.kr'
    title = 'Mungshil Cloud Email Verification Code: {}'.format(rand_code)
    
    # msg = Message(title, sender='mungshilcloud@gmail.com', recipients=[name])
    msg = Message(title, sender='mungshilcloud@gmail.com', recipients=[name])


    # print('111111111111111111111')
    
    # msg.body = rand_code
    # msg.extra_headers(rand_code)

    msg.html="""
                <img src="https://avatars.githubusercontent.com/u/86836065?s=40&v=4">
                <h1>Welcome!<h1>
             """

    # msg.html = render_template('test.html')
    # print(msg)


    
    print(rand_code)
    print('222222222222222222222')
    mail.send(msg) 
    print('333333333333333333333')
    return 'Sent'

if __name__ == '__main__' :
    app.run()