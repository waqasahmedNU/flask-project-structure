from flask import request, make_response, jsonify
from flask_restful import Resource, current_app as app


class ExampleResource(Resource):

    def __init__(self):
        pass

    def get(self):
        return make_response(jsonify({
            'messages': 'success',
            'method': 'GET'
        }))

    def post(self):
        return make_response(jsonify({
            'messages': 'success',
            'method': 'POST'
        }))

    def put(self):
        return make_response(jsonify({
            'messages': 'success',
            'method': 'PUT'
        }))

    def delete(self):
        return make_response(jsonify({
            'messages': 'success',
            'method': 'DELETE'
        }))