import keyring
from flask import jsonify
from datetime import datetime, timedelta
import pandas as pd

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

def date_n_days_ago(n):
    date = datetime.now() - timedelta(days=n)
    return date

def generate_li(endpoint_list):
    li_elements = [f'<li><code><a href = "/api/{x}">{x}</a></code></li>' for x in endpoint_list]
    li_html = '\n'.join(li_elements)
    return li_html

def trim_str(str):
    if str.startswith('application.'):
        return str.replace('application.', '', 1)
    else:
        return str
    
def csv_to_table(csv_path, table_name, engine):
    df = pd.read_csv(csv_path)
    df.replace('..', None, inplace=True)
    df.rename(columns=lambda x: x.lower(), inplace=True)
    df.to_sql(table_name, engine, if_exists='replace', index=False)


