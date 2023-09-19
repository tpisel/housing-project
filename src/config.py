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
        "name": "dwellings",
        "table": "vic_selected_census",
        "columns": [
            "lga_code_2021",
            "OPDs_Separate_house_Dwellings",
            "OPDs_SD_r_t_h_th_1_sty_Dwgs",
            "OPDs_SD_r_t_h_th_2_m_sty_Dwgs",
            "OPDs_SD_r_t_h_th_Tot_Dwgs",
            "OPDs_F_ap_I_1or2_sty_blk_Ds",
            "OPDs_F_ap_I_3_sty_blk_Dwgs",
            "OPDs_F_ap_I_4to8_sty_blk_Ds",
            "OPDs_F_ap_I_9_m_sty_blk_Ds",
            "OPDs_Flt_apt_Att_house_Ds",
            "OPDs_Flt_apart_Tot_Dwgs",
            "OPDs_Other_dwelling_Tot_Dwgs",
            "OPDs_Tot_OPDs_Dwellings",
            "Unoccupied_PDs_Dwgs",
            "Total_PDs_Dwellings",
            "Total_Total"
            ]
    },
  {
        "name": "people_dwellings",
        "table": "vic_selected_census",
        "columns": [
            "lga_code_2021",
            "OPDs_Separate_house_Persons",
            "OPDs_SD_r_t_h_th_1_sty_Psns",
            "OPDs_SD_r_t_h_th_2_m_sty_Psns",
            "OPDs_SD_r_t_h_th_Tot_Psns",
            "OPDs_F_ap_I_1or2_sty_blk_Ps",
            "OPDs_F_ap_I_3_sty_blk_Psns",
            "OPDs_F_ap_I_4to8_sty_blk_Ps",
            "OPDs_F_ap_I_9_m_sty_blk_Ps",
            "OPDs_Flt_apt_Att_house_Ps",
            "OPDs_Flt_apart_Tot_Psns",
            "OPDs_Other_dwelling_Tot_Psns",
            "OPDs_Tot_OPDs_Persons",
            "Unoccupied_PDs_Psns",
            "Total_PDs_Persons",
            "Total_Total"
            ]
    },

    {
        "name": "planning_applications", 
        "table": "planning_application",
        "columns": ["id",
                    "info_url", 
                    "description", 
                    "date_received", 
                    "lat", 
                    "lng", 
                    "lga_fullname"]
    },
    
    {
        "name": "cleaned_planning_applications", 
        "table": "single_storey",
        "columns": [
            "id", 
            "description",
            "lat", 
            "lng", 
            "lga_fullname",
            "storey"]
    }
]


# global settings

from src.utils import date_n_days_ago

parameters = {
    'api_page_limit': 1, #40, # leave at 2 for testing
    'api_age_limit': date_n_days_ago(365),
    'api_wait_s': 0.05
}
