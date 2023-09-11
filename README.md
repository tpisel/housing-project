# housing-project


Bootcamp project 3 

**Contributors**

- Rhiannyn Geeson
- Tom Pisel
- Sagar Bora
- Raviska

## Topic 

// Housing / planning to expand on

idea is to have all the LGAs in melbourne, and overlay census data and planning permits

maybe allow zooming in when an LGA is selected and regex / filtering on descriptions

Could color / tag them based on content, see example in `Week 15 / 3 / 02-Stu_CitiBike_Leaflet`

some kind of time series (perhaps from census data)

must use leaflet / plotly and something new 

maybe encode in geojson


For inspiration: [Housing density in Melbourne](https://chartingtransport.com/2023/06/10/how-is-population-density-changing-in-australian-cities-2023-update/)

## Architecture

This is an end-to-end data visualisation application that retrieves data from an API, combines it with existing data sources, exposes the combined data via API endpoints, and enables it to be visualised with an interactive front-end.

Two processes must be running for the application to work, the PostgreSQL database and the Flask webserver that serves the API requests.


// put an image in here 


### Postgres Database

Data


## Pre-requisites

You will need to have Postgres and `psql` installed. A `requirements.txt` has been provided in the root directory. The first time you run the app, you will be asked for an API key from PlanningAlerts. Sing up to obtain a free API key [here](https://www.planningalerts.org.au/api/howto). The script will save the API key on your local keyring.



// will need to store API key (use `keyring` in sh script if doesn't already exist)



## Initialisation

To run the app, run `sh initialise.sh` in terminal from the project root directory. This creates a database `melbournehousingdb` under the `postgres` user, loads census static files in `/resources` to the database, starts the flask webserver to transform and serve this data via scripts in `/src`, and opens up the web page `index.html`. This webpage renders the data via JavaScript also in `/src`.

### `/src` scripts

- ex.py
- ex.py 


### `/resources` data

Data from the [2021 Census](https://www.abs.gov.au/census/find-census-data/datapacks?release=2021&product=GCP&geography=LGA&header=S):

- `2021Census_G02_VIC_LGA.csv` contains 'Selected Medians and Averages'
- `2021Census_G34_VIC_LGA.csv` contains 'Number of Motor Vehicles by Dwellings'
- `2021Census_G36_VIC_LGA.csv` contains 'Dwelling Structure'
- `2021Census_G41_VIC_LGA.csv` contains 'Dwelling Structure by Number of Bedrooms'

As the column names in these files are are abbreviated, a reference document with longer column names is included in `cell_descriptors.csv`

## Disclaimer

_disclaimer about external resources used_


