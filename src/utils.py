import keyring
from flask import jsonify

def get_secret(secret):
    match secret:
        case 'planningalerts':
            return keyring.get_password('planning_alerts', 'api_key')
        case 'postgres':
            return keyring.get_password('postgresql', 'postgres')
        case _:
            raise Exception("key not found")

def jsonify_from_result(result_from_execute):
    column_names = result_from_execute.keys()
    results_list = [dict(zip(column_names, row)) for row in result_from_execute]
    return jsonify(results_list)

