# configuration dictionary that determines what gets exported from the API endpoints

# each endpoint listed here will be a flask route and return data from the tables in the database

# localhost/census

endpoints = [
    {
        "name": "census",
        "table": "sqltable",
        "columns": ["LGA_CODE_2021","Median_mortgage_repay_monthly"]
    },
    {
        "name": "planning",
        "table": "planning_application",
        "columns": ["info_url", "comment_url", "date_received"]
    }
]


