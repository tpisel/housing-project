# configuration dictionary that determines what gets exported from the API endpoints

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