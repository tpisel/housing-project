# housing-project

Monash data bootcamp project 3

**Contributors**

- Rhiannyn Geeson
- Tom Pisel
- Sagar Bora
- Raviska Marasingha

## Topic 

// Mapping planning applications, housing and cars

![](img/header.jpg)


We will investigate all the LGAs in Melbourne, and overlay census data and planning permits, allowing for zoom into an LGA on an interactive map which, when clicked, refreshes the charts to reflect the targetted LGA information.
We have used Leaflet, Highcharts (not covered in class materials), Python, CSS, SQL.


## Architecture

This is an end-to-end data visualisation application that retrieves data from an API, combines it with existing data sources, exposes the combined data via API endpoints, and enables it to be visualised with an interactive front-end.


## Pre-requisites

You will need to have Postgres installed. A `requirements.txt` has been provided in the root directory. The first time you run the app, you will be asked for your postgres password and an API key from PlanningAlerts. Sign up to obtain a free API key [here](https://www.planningalerts.org.au/api/howto). The script will save the API key on your local keyring.



## Initialisation

To run the app the first time, run `python initialise.py --createdb` in terminal from the project root directory. Running this script with the `--createdb` tag:

1. Requests and saves the credentials for the `postgres` user and PlanningAlerts API key
2. Creates a database `melbournehousingdb` under the `postgres` user
3. Cleans and loads census data files in `/resources` to the database
4. Pulls data from the PlanningAlerts API and loads it to the database
5. Starts the flask webserver to transform and serve this data via API endpoints at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
6. Opens up the web page `index.html` which renders data from the endpoints via JavaScript in `/src`

Once the database has been created, you can run `python initialise.py` without the tag to only start the flask server and open the web page.

### `/src` scripts

- `main.py` the flask app that reads data from the database and provides API endpoints
- `config.py` a configuration file that determines what is exposed from the database
- `callapi.py` calls the planning alerts api and saves the data in the database
- `utils.py` includes misc. tooling and convenience functions


### `/resources` data

Data from the [2021 Census](https://www.abs.gov.au/census/find-census-data/datapacks?release=2021&product=GCP&geography=LGA&header=S):

- `2021Census_G02_VIC_LGA.csv` contains 'Selected Medians and Averages'
- `2021Census_G34_VIC_LGA.csv` contains 'Number of Motor Vehicles by Dwellings'
- `2021Census_G36_VIC_LGA.csv` contains 'Dwelling Structure'
- `2021Census_G41_VIC_LGA.csv` contains 'Dwelling Structure by Number of Bedrooms'
- `2021_ASGS_Non_ABS_Structures.csv` contains the meaningful LGA names to join against the census codes

As the column names in these files are are abbreviated, a reference document with longer column names is included in `cell_descriptors.csv`

Data from the PlanningApplications API: https://www.planningalerts.org.au/api/howto
This data is collected by their API, and is free to the public for non-commercial use.

GeoScape LGA data: Incorporates or developed using Administrative Boundaries © Geoscape Australia licensed by the Commonwealth of Australia under Creative Commons Attribution 4.0 International licence (CC BY 4.0)
**This dataset was originally found on data.gov.au "VIC Local Government Areas - Geoscape Administrative Boundaries". Please visit the source to access the original metadata of the dataset:
https://data.gov.au/data/dataset/bdf92691-c6fe-42b9-a0e2-a4cd716fa811


## Referenced sources and materials

Materials other than those covered in class are as follows:

Referred to https://popsql.com/learn-sql/sql-server/how-to-have-multiple-counts-in-sql-server for guidance in compiling the regex for data cleaning
ChatGPT was used to identify bugs in database cleaning and offer potential solutions (not very useful)
D3 and Python documentation of data cleaning
StackOverfloww


