from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mungshilcloud@gmail.com'
app.config['MAIL_PASSWORD'] = 'andtlfrnfma!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index() :
    print('1111')
    msg = Message('Welcome MungshilCloud', sender='mungshilcloud@gmail.com', recipients=['msj00130@gmail.com'])
    print('2222')
    print(msg)
    msg.body = '天下無敵 MungshilCloud'
    print('3333')
    mail.send(msg)
    print('4444')
    return 'Sent'

if __name__ == '__main__' :
    app.run()