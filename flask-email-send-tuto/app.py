from os import name
from flask import Flask, render_template, request
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
    return render_template('home.html')

@app.route('/send', methods=['POST'])
def send_email():
    name = request.form['Receiver']
    title = request.form['Head']
    message = request.form['Body']
    print(name)
    print(title)
    print(message)
    
    print('1111')
    msg = Message(title, sender='mungshilcloud@gmail.com', recipients=[name])
    print('2222')
    print(msg)
    msg.body = message
    print('3333')
    mail.send(msg)
    print('4444')
    return 'Sent'

if __name__ == '__main__' :
    app.run()