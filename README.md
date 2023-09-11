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

some kind of time series (perhaps from census data)


## Architecture

This is an end-to-end data visualisation application that retrieves data from an API, combines it with existing data sources, exposes the combined data via API endpoints, and enables it to be visualised with an interactive front-end.

Two processes must be running for the application to work, the PostgreSQL database and the Flask webserver that serves the API requests.



// put an image in here



## Pre-requisites

You will need to have Postgres and `psql` installed. A `requirements.txt` has been provided in the root directory. The first time you run the app, you will be asked for two API keys:




// how to store secrets for the API (use `keyring`)



```sh
keyring set 
```


## Initialisation

To run the app, run `sh initialise.sh` in terminal from the project root directory. This creates a database `melbournehousingdb` under the `postgres` user, loads census static files in `/resources` to the database, starts the flask webserver to transform and serve this data via scripts in `/src`, and opens up the web page `index.html`. This webpage renders the data via JavaScript also in `/src`.

### `/src` scripts

- ex.py
- ex.py 


### `/resources` data

- ex.csv
- ex.csv

## Disclaimer

_disclaimer about external resources used_


