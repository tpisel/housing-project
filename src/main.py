# the main flask app 

import pandas as pd
from src.config import endpoints
from src.utils import get_secret, jsonify_from_result, generate_li
from sqlalchemy import create_engine, MetaData, text
from flask import Flask

app = Flask(__name__)

engine = create_engine(f"postgresql://postgres:{get_secret('postgres')}@localhost/melbournehousingdb")
metadata = MetaData()
metadata.bind = engine

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

for endpoint in endpoints:
    app.add_url_rule(f'/api/{endpoint["name"]}', endpoint['name'], generate_endpoint(endpoint))

###############################################################

# ADD ANY ADDITIONAL ROUTES HERE! (and your transform scripts)

# example to copy
@app.route('/api/exampleroute')
def exampleroute():
    query = 'select * from vic_selected_census limit 1'
    with engine.connect() as conn:
        result = conn.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        # ADD PANDAS TRANSFORMS HERE
        return df.to_json(orient='records', date_format='iso')


# example to copy
@app.route('/api/transformed_census_dwellings')
def exampleroute():
    query = 'select * from vic_selected_census limit 1'
    with engine.connect() as conn:
        result = conn.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        # ADD PANDAS TRANSFORMS HERE
        return df.to_json(orient='records', date_format='iso')
    
    

# N PER STOREY/COUNCIL


@app.route('/api/nstories')
def nstories():
    query = 'select lga_fullname, storey, count(*) as applications from all_storey group by 1, 2, 3, 4'
    with engine.connect() as conn:
        result = conn.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        # ADD PANDAS TRANSFORMS HERE
        return df.to_json(orient='records', date_format='iso')





# ADD YOUR ENDPOINTS HERE to have them show up on the home page:

root_menu_dict = [
    'exampleroute',
    'nstories'
]




###############################################################

generated_routes = [e['name'] for e in endpoints]
root_menu_dict = root_menu_dict + generated_routes

@app.route('/')
def homepage():

    endpoint_links = generate_li(root_menu_dict)
    
    html = f'''
    <h1> Planning Application API homepage </h1>
    <h2> Available endpoints: </h2>
    <ul>
        {endpoint_links}
    </ul>
    '''
    return html


if __name__ == '__main__':
    app.run()