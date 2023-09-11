
# request the postgres password and api key

echo "Please enter the PostgreSQL password for the 'postgres' user:"
read -s PGPASSWORD
export PGPASSWORD

echo "\nPlease enter the API key from PlanningAlerts.org.au:"
read -s PLANNINGALERTSKEY
export PLANNINGALERTSKEY


# fix the null values in the Census CSVs encoded as `..`

mkdir -p resources/cleaned
for file in ./resources/2021Census*; do
    [ -e "$file" ] || continue
    base=$(basename "$file")
    sed 's/\.\./\\N/g' "$file" > "./resources/cleaned/$base"
done


# create the postgres database if it doesn't exist

DB_NAME=melbournehousingdb

DB_EXISTS=$(psql -h localhost -U postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'")

if [ "$DB_EXISTS" = "1" ];
then
    echo "Database $DB_NAME already exists. Exiting."
    exit 1
else
    createdb -h localhost -U postgres $DB_NAME
fi

psql -h localhost -U postgres -d $DB_NAME -f Database/crowdfunding_db_schema.sql



# create the tables



# upload data from CSVs and create joined census view for querying with transforms



# query some data from api (with status bars)



# start flask app in background process



# open index.html




# cleanup

unset PGPASSWORD
