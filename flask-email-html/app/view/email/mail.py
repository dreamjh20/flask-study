from flask_restful import Resource
from flask import Flask, jsonify, request

class SendEmail(Resource):
    def post(self):
        print("EMAIL")
        
        return jsonify({"message":"succeed"})