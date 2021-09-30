from flask import Blueprint, jsonify
from flask_restful import Api

email_blueprint = Blueprint('home', __name__, url_prefix='/')
email_api = Api(email_blueprint)

from .mail import SendEmail
email_api.add_resource(SendEmail, '/email')