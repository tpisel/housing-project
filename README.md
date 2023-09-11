# housing-project


Bootcamp project 3 

**Contributors**

- Rhiannyn Geeson
- Tom Pisel
- Sagar Bora
- Raviska Marasingha

## Topic 

// **Housing** / to expand on intro here

![](img/header.jpg)

idea is to have all the LGAs in melbourne, and overlay census data and planning permits

maybe allow zooming in when an LGA is selected and regex / filtering on descriptions

Could color / tag them based on content, see example in `Week 15 / 3 / 02-Stu_CitiBike_Leaflet`

some kind of time series perhaps, each json object has a timestamp attached to it

must use leaflet / plotly and something new 

maybe encode in geojson

example API response

```json
{
"application": {
"id": 3005309,
"council_reference": "0062/20 - SC1 (VicSmart)",
"date_scraped": "2023-09-06T05:44:03.406Z",
"address": "29 Murray Street, Prahran VIC 3181",
"description": "Secondary Consent Amendment to approved plans - The proposed change is to reduce the height of the fence from 1.95m to 1.5m. All other aspects to remain the same.",
"info_url": "https://eplanning.stonnington.vic.gov.au/EPlanning/Public/ViewActivity.aspx?refid=0062/20%20-%20SC1%20(VicSmart)",
"comment_url": null,
"date_received": "2023-09-06",
"on_notice_from": null,
"on_notice_to": null,
"lat": -37.8501144,
"lng": 144.9995149,
"authority": {
"full_name": "City of Stonnington"
}
}
}
```


For inspiration: [Housing density in Melbourne](https://chartingtransport.com/2023/06/10/how-is-population-density-changing-in-australian-cities-2023-update/)

## Architecture

This is an end-to-end data visualisation application that retrieves data from an API, combines it with existing data sources, exposes the combined data via API endpoints, and enables it to be visualised with an interactive front-end.

Two processes must be running for the application to work, the PostgreSQL database and the Flask webserver that serves the API requests.


// put an image in here 


## Pre-requisites

You will need to have Postgres and `psql` installed. A `requirements.txt` has been provided in the root directory. The first time you run the app, you will be asked for an API key from PlanningAlerts. Sing up to obtain a free API key [here](https://www.planningalerts.org.au/api/howto). The script will save the API key on your local keyring.


// will need to store API key (use `keyring` in sh script if doesn't already exist)



## Initialisation

To run the app, run `sh initialise.sh` in terminal from the project root directory. This creates a database `melbournehousingdb` under the `postgres` user, loads census static files in `/resources` to the database, starts the flask webserver to transform and serve this data via scripts in `/src`, and opens up the web page `index.html`. This webpage renders the data via JavaScript also in `/src`.

### `/src` scripts

- ex.py
- ex.js
- ex.css


### `/resources` data

Data from the [2021 Census](https://www.abs.gov.au/census/find-census-data/datapacks?release=2021&product=GCP&geography=LGA&header=S):

- `2021Census_G02_VIC_LGA.csv` contains 'Selected Medians and Averages'
- `2021Census_G34_VIC_LGA.csv` contains 'Number of Motor Vehicles by Dwellings'
- `2021Census_G36_VIC_LGA.csv` contains 'Dwelling Structure'
- `2021Census_G41_VIC_LGA.csv` contains 'Dwelling Structure by Number of Bedrooms'
- `georef-australia-local-government-area.csv` contains 2021 shape files and LGA names from [opendatasoft](https://public.opendatasoft.com/explore/dataset/georef-australia-local-government-area/table/?disjunctive.ste_code&disjunctive.ste_name&disjunctive.lga_code&disjunctive.lga_name)

As the column names in these files are are abbreviated, a reference document with longer column names is included in `cell_descriptors.csv`

## Disclaimer

_disclaimer about external resources used_


