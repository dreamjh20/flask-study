from app.view.send.send import Send
from flask import Blueprint
from flask_restful import Api

send_blueprint = Blueprint("send", __name__)
api = Api(send_blueprint)

api.add_resource(Send, "/send")