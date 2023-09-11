
# request the postgres password and api key


# fix the null values in the Census encoded as `..`
for file in ./resources/2021Census*; do
    [ -e "$file" ] || continue
    base=$(basename "$file")
    sed 's/\.\./\\N/g' "$file" > "./resources/cleaned/$base"
done



# create the postgres database if it doesn't exist



# create the tables



# upload data from CSVs and create joined census view for querying with transforms



# query some data from api (with status bars)



# start flask app in background process



# open index.html




