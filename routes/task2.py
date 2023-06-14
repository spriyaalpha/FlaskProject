from flask import Flask, request, jsonify,Blueprint
from constants.constants import *
from dals.task2 import register_dals,login_dals

task2_blueprint = Blueprint('api', __name__)


users = {}  

@task2_blueprint.route(REGISTER, methods=['POST'])
def register():
    try:
        data = request.get_json()
        return register_dals(data)
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'})

@task2_blueprint.route(LOGIN, methods=['POST'])
def login():
    try:
        data = request.get_json()
        return login(data)
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'})


