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
    },
    {
        "name": "planning_applications", 
        "table": "planning_application",
        "columns": ["info_url", "comment_url", "date_received"]
    }
]

# global settings

from src.utils import date_n_days_ago

parameters = {
    'api_page_limit': 2, #40, # leave at 2 for testing
    'api_age_limit': date_n_days_ago(365),
    'api_wait_s': 0.1
}
