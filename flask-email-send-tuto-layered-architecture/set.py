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
    rec_name = request.form['Receiver']
    title = request.form['Head']
    message = request.form['Body']
    print(rec_name)
    print(title)
    print(message)
    
    print('1111')
    msg = Message(title, sender='mungshilcloud@gmail.com', recipients=[rec_name])
    print('2222')
    print(msg)
    msg.body = message
    print('3333')
    mail.send(msg)
    print('4444')
    return 'Sent'