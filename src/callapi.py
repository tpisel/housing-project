# function to call api

# will need to upsert probably to avoid dupes?

# easy way to do it is save as csv and then pull in from there



import pandas as pd
from sqlalchemy import create_engine
from utils import get_secret, datestr_n_days_ago, trim_str
import requests

engine = create_engine(f"postgresql://postgres:{get_secret('postgres')}@localhost/melbournehousingdb")

# querying function, returns dataframe

def query_api(lga,page=1):
    key = get_secret('planningalerts')
    url = f"https://api.planningalerts.org.au/authorities/{lga}/applications.json?key={key}&page={page}"
    response = requests.get(url)
    if response.status_code == 200:
        df = pd.json_normalize(response)
        df.rename(columns=trim_str, inplace=True)
        return df
    else:
        print(f"Failed to retrieve data for page {page} of {lga}. HTTP Status code: {response.status_code}")

# loop through endpoints


# want to query an endpoint until we hit x pages or go back y days, whichever comes first
page_limit = 40
age_limit = datestr_n_days_ago(30)
lgas = ['moreland_city','mornington_peninsula','manningham'] # for testing, we'll later pull a unique list of url_names from database

combined_df = pd.DataFrame()

for lga in lgas:
    
    lga_df  = pd.DataFrame()
    page = 1

    while page < page_limit:
        if (lga_df.date_received.min() < age_limit):
            break
        page_df = query_api(lga,page)
        page = page + 1


    # concat df responses


# confirm each row is unique





# write data to database

combined_df.to_sql('planning_application', engine, if_exists='replace', index=False)
