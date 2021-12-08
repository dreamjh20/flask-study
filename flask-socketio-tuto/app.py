from flask import Flask, app
from flask_socketio import SocketIO, send

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)