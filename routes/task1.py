from flask import request, jsonify,Blueprint
from constants.constants import *
from dals.task1 import calculate_sum_dal,concatenate_strings_dal
task1_blueprint = Blueprint('api', __name__)

@task1_blueprint.route(SUM, methods=['POST'])
def calculate_sum():
    try:
        data = request.get_json()  
        return calculate_sum_dal(data)            
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'})
    
@task1_blueprint.route(CONCATENATE, methods=['POST'])
def concatenate_strings():
    try:
        data = request.get_json()
        return concatenate_strings_dal(data)
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'})    
    