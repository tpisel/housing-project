# function to call api

# will need to upsert probably to avoid dupes?

# easy way to do it is save as csv and then pull in from there



import pandas as pd
from sqlalchemy import create_engine
from utils import get_secret, datestr_n_days_ago

engine = create_engine(f"postgresql://postgres:{get_secret('postgres')}@localhost/melbournehousingdb")

# Collect data from the endpoints and combine them into a dataframe


def query_api(lga,page=1):
    key = get_secret('planning_alerts')
    url = "https://api.planningalerts.org.au/authorities/{lga}/applications.json?key={key}&page={page}"

    # query and turn into dataframe
    

    return pd.DataFrame()




page_limit = 40
age_limit = datestr_n_days_ago(30)

lgas = ['moreland_city','mornington_peninsula','manningham'] # for testing, we'll pull a unique list of url_names from database

df = pd.DataFrame()

for lga in lgas:
    
    page = 1
    while page < 40 & df.date_received.min() < age_limit:
        df_page = query_api(lga,page)



    # concat df responses


# confirm each row is unique

# write data to database

df.to_sql('planning_application', engine, if_exists='replace', index=False)
