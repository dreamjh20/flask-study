import re
from flask_restful import Resource
from flask import Flask, jsonify, request, json

class SendEmail(Resource):
    def post(self):

        j_son= request.get_json()
        print(request.is_json)

        return 'json'