# configuration dictionary that determines what gets exported from the API endpoints

# Each entry here will create a route at /api/`name` and return json from the selected columns and database table

endpoints = [
    {
        "name": "mortgages",
        "table": "vic_selected_census",
        "columns": [
            "lga_code_2021",
            "median_mortgage_repay_monthly"
            ]
    },
    {
        "name": "cars",
        "table": "vic_selected_census",
        "columns": [
            "num_mvs_per_dweling_0_mvs",
            "num_mvs_per_dweling_1_mvs",
            "num_mvs_per_dweling_2_mvs",
            "num_mvs_per_dweling_3_mvs"
            ]
    }

    # to come, once I add the api ingest

    # {
    #     "name": "planning", 
    #     "table": "planning_application",
    #     "columns": ["info_url", "comment_url", "date_received"]
    # }
]


