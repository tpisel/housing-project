# the main flask app 


from config import endpoints
from utils import get_secret
from sqlalchemy import create_engine, Table, MetaData
from flask import Flask, jsonify
# import pandas as pd



app = Flask(__name__)
engine = create_engine(f"postgresql://postgres:{get_secret('postgres')}@localhost/melbournehousingdb")

# i might need to abstract this to orm dynamically across tables
metadata = MetaData(bind=engine)
selected_medians = Table('selected_medians', metadata, autoload=True, autoload_with=engine)

@app.route('/')
def home():
    with engine.connect() as conn:
        result = conn.execute(selected_medians.select())
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df.to_html()


if __name__ == '__main__':
    app.run()