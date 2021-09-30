from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

def html_email_blueprint(app : Flask):
    from .view.email import email_blueprint
    app.register_blueprint(email_blueprint)


def create_app() -> Flask:
    app = Flask(__name__)
    
    html_email_blueprint(app)

    return app