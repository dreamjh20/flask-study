from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketIO = SocketIO(app)

@socketIO.on('message')
def message(msg):
    print("MESSAGE: " + msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketIO.run(app)