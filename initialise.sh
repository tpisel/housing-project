#!/bin/bash

initialise_proj() {

    # request the postgres password and api key
    echo "Please enter the PostgreSQL password for the 'postgres' user:"
    read -s PGPASSWORD
    export PGPASSWORD

    echo "\nPlease enter the API key from PlanningAlerts.org.au:"
    read PLANNINGALERTSKEY
    export PLANNINGALERTSKEY


    # fix the null values in the Census CSVs encoded as `..` and save in resources/cleaned
    mkdir -p resources/cleaned
    for file in ./resources/2021Census*; do
        [ -e "$file" ] || continue
        base=$(basename "$file")
        sed 's/\.\./''/g' "$file" > "./resources/cleaned/$base"
    done


    # create the postgres database if it doesn't exist
    DB_NAME=melbournehousingdb

    echo "creating database $DB_NAME..."

    DB_EXISTS=$(psql -h localhost -U postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'")

    if [ "$DB_EXISTS" = "1" ];
    then
        echo "Database $DB_NAME already exists."
        echo "Do you want to drop and recreate the database? [Y/n]"
        read drop
        if [[ $drop =~ ^([yY])$ ]]; then  
            echo "Dropping database $DB_NAME..."
            psql -h localhost -U postgres -c "DROP DATABASE $DB_NAME WITH (FORCE);"
            echo "Creating database $DB_NAME..."
            createdb -h localhost -U postgres $DB_NAME
        else
            echo "Exiting project set up"
            exit 1
        fi
    else
        createdb -h localhost -U postgres $DB_NAME
    fi

    # create the tables
    psql -h localhost -U postgres -d $DB_NAME -f src/schema.sql

    # upload data from CSVs and create joined census view for querying with transforms
    psql -h localhost -U postgres -d $DB_NAME -f src/psql-scripts.sql

    # persist the credentials so we don't need to ask next time
    python src/credentials.py

    # query some data from api (with status bars) -- some number of pages as default
    python src/callapi.py

    # cleanup
    unset PGPASSWORD
    unset PLANNINGALERTSKEY
}

# check if we want to create the database
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --createdb) 
            initialise_proj
            shift 
            ;;
        *) 
            echo "Unknown parameter passed: $1"; 
            exit 1 
            ;;
    esac
    shift
done

# run the app
export FLASK_APP=src/main.py
flask run #& open index.html
open http://127.0.0.1:5000 # just for testing to see the flask routes
