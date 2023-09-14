# housing-project

Monash data bootcamp project 3

**Contributors**

- Rhiannyn Geeson
- Tom Pisel
- Sagar Bora
- Raviska Marasingha

## Topic 

// **Mapping planning applications** / to expand on intro here

![](img/header.jpg)


idea is to have all the LGAs in melbourne, and overlay census data and planning permits

maybe allow zooming in when an LGA is selected and regex / filtering on descriptions

Could color / tag them based on content, see example in `Week 15 / 3 / 02-Stu_CitiBike_Leaflet`

some kind of time series perhaps, each json object has a timestamp attached to it

must use leaflet / plotly and something new 


For inspiration: [Housing density in Melbourne](https://chartingtransport.com/2023/06/10/how-is-population-density-changing-in-australian-cities-2023-update/)


## Architecture

This is an end-to-end data visualisation application that retrieves data from an API, combines it with existing data sources, exposes the combined data via API endpoints, and enables it to be visualised with an interactive front-end.


// put a diagram in here 


## Pre-requisites

You will need to have Postgres and `psql` installed. A `requirements.txt` has been provided in the root directory. The first time you run the app, you will be asked for your postgres password and an API key from PlanningAlerts. Sign up to obtain a free API key [here](https://www.planningalerts.org.au/api/howto). The script will save the API key on your local keyring.



## Initialisation

To run the app the first time, run `sh initialise.sh --createdb` in terminal from the project root directory. Running this script with the `--createdb` tag:

1. Requests and saves the credentials for the `postgres` user and PlanningAlerts API key
2. Creates a database `melbournehousingdb` under the `postgres` user
3. Cleans and loads census data files in `/resources` to the database
4. Pulls data from the PlanningAlerts API and loads it to the database
5. Starts the flask webserver to transform and serve this data via API endpoints at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
6. Opens up the web page `index.html` which renders data from the endpoints via JavaScript in `/src`

Once the database has been created, you can run `sh initialise.sh` without the tag to only start the flask server and open the web page.

### `/src` scripts

- `main.py` the flask app that reads data from the database and provides API endpoints
- `config.py` a configuration file that determines what is exposed from the database
- `callapi.py` calls the planning alerts api and saves the data in the database
- `credentials.py` saves credentials on the keyring
- `utils.py` includes misc. tooling and convenience functions
- `schema.sql` the database schema
- `psql-scripts.sql` database commands to upload data and create views for consumption


### `/resources` data

Data from the [2021 Census](https://www.abs.gov.au/census/find-census-data/datapacks?release=2021&product=GCP&geography=LGA&header=S):

- `2021Census_G02_VIC_LGA.csv` contains 'Selected Medians and Averages'
- `2021Census_G34_VIC_LGA.csv` contains 'Number of Motor Vehicles by Dwellings'
- `2021Census_G36_VIC_LGA.csv` contains 'Dwelling Structure'
- `2021Census_G41_VIC_LGA.csv` contains 'Dwelling Structure by Number of Bedrooms'
- `2021_ASGS_Non_ABS_Structures.csv` contains the meaningful LGA names to join against the census codes

As the column names in these files are are abbreviated, a reference document with longer column names is included in `cell_descriptors.csv`

## Disclaimer

_disclaimer about external resources used_


