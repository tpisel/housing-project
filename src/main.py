# the main flask app 

import pandas as pd
from config import endpoints
from utils import get_secret, jsonify_from_result
from sqlalchemy import create_engine, Table, MetaData, text
from flask import Flask

app = Flask(__name__)
engine = create_engine(f"postgresql://postgres:{get_secret('postgres')}@localhost/melbournehousingdb")

# i might need to abstract this to orm dynamically across tables

metadata = MetaData()
metadata.bind = engine
selected_medians = Table('selected_medians', metadata, autoload_with=engine)

# function to take an endpoint from the config and return the right data
def generate_endpoint(endpoint):
    def generated_endpoint():        
        table = endpoint["table"]
        columns = ', '.join(endpoint["columns"])
        query_string = f"SELECT {columns} FROM {table}" # the query 
        
        with engine.connect() as conn:
            result = conn.execute(text(query_string))
            return jsonify_from_result(result)
    
    return generated_endpoint

# Generate endpoints
for endpoint in endpoints:
    app.add_url_rule(f'/api/{endpoint["name"]}', endpoint['name'], generate_endpoint(endpoint))


if __name__ == '__main__':
    app.run()