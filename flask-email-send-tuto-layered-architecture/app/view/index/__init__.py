from app.view.index.index import Index
from flask import Blueprint
from flask_restful import Api

index_blueprint = Blueprint("index", __name__)
api = Api(index_blueprint)

api.add_resource(Index, "/")
