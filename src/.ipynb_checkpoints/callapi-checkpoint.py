# function to call the planning alerts api

import pandas as pd
from sqlalchemy import create_engine, MetaData, text
from utils import get_secret, trim_str
from config import parameters
import requests
import sys
import time

engine = create_engine(f"postgresql://postgres:{get_secret('postgres')}@localhost/melbournehousingdb")
metadata = MetaData()
metadata.bind = engine


# querying function, returns dataframe
def query_api(lga,page=1):
    key = get_secret('planningalerts')
    url = f"https://api.planningalerts.org.au/authorities/{lga}/applications.json?key={key}&page={page}"
    response = requests.get(url)
    
    if response.status_code == 200:    
        df = pd.json_normalize(response.json())
        
        df.rename(columns=trim_str, inplace=True)
        return df
    elif response.status_code == 401:
        sys.exit('An incorrect https://www.planningalerts.org.au/ API key has been provided, exiting.')
    else:
        print(f"Failed to retrieve data for page {page} of {lga}. HTTP Status code: {response.status_code}")


# want to query an endpoint until we hit x pages or go back y days, whichever comes first
page_limit = parameters['api_page_limit']
age_limit = parameters['api_age_limit']
api_wait_s = parameters['api_wait_s']


# retrieve list of lgas

with engine.connect() as conn:
    result = conn.execute(text('select distinct url_name from local_gov_area where url_name is not null'))
    result_raw = result.fetchall()
    lgas = [x[0] for x in result_raw]


# loop through endpoints

print('\nQuerying the Planning Alerts API:\n')

combined_df_array = []
lga_count = 1

for lga in lgas:
    
    lga_df_array = []
    page = 1

    while page <= page_limit:
        
        print(f"  LGA {lga_count} of {len(lgas)}: '{lga}' - retrieving page {page}")


        page_df = query_api(lga,page)
        page_df.rename(columns={'authority.full_name': 'lga_fullname'}, inplace=True)
        page_df['lga_urlname'] = lga

        time.sleep(api_wait_s)
        
        lga_df_array.append(page_df)

        page = page + 1

        dates = pd.concat(lga_df_array)['date_received']
        min_date = pd.to_datetime(dates).min()

        if (min_date < age_limit): # exit loop if we have an old enough record
            break

    combined_df_array.append(pd.concat(lga_df_array))
    lga_count = lga_count+1


combined_df = pd.concat(combined_df_array).drop_duplicates()

# write data to database
print('\nWriting to planning_application table')
combined_df.to_sql('planning_application', engine, if_exists='replace', index=False)
print('Done writing to database\n')

