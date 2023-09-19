# create tables and views in the database for querying

from sqlalchemy import create_engine, text


def run_ctas(engine):

    def execute_sql(query):
            with engine.connect() as connection:
                result = connection.execute(text(query))
                connection.commit()

    query_list = [
    '''
    CREATE VIEW vic_selected_census AS
    SELECT * -- this bit can be edited to create simple transformed columns
    FROM local_gov_area
        LEFT JOIN dwellings_by_bedroom USING (lga_code_2021)
        LEFT JOIN dwelling_structure USING (lga_code_2021)
        LEFT JOIN selected_medians USING (lga_code_2021)
        LEFT JOIN vehicles_per_dwelling USING (lga_code_2021)
    WHERE LEFT(lga_code_2021, 4) = 'LGA2'
    ''',
    '''
    CREATE VIEW double_storeys AS
    SELECT id, description, lat, lng, lga_fullname, 2 as storey
    FROM planning_application
    WHERE description ~ 'double storey|two storey|2\) storey'
    AND description ~ 'dwelling|residential';
    ''',
    '''
    CREATE VIEW three_storeys AS
    SELECT id, description, lat, lng, lga_fullname, 3 as storey
    FROM planning_application
    WHERE description ~ 'three storey|three storey|3\) storey'
    AND description ~ 'dwelling|residential';
    ''',
    '''
    CREATE VIEW single_storey AS
    SELECT id, description, lat, lng, lga_fullname, 1 as storey
    FROM planning_application
    WHERE description ~ 'single storey|one storey|1\) storey'
    AND description ~ 'dwelling|residential'
    AND description ~ 'development';
    ''',
    '''

    CREATE VIEW combined_view AS
    SELECT id, description, lat, lng, lga_fullname, 5 as storey
    FROM planning_application
    WHERE description ~ 'five storey|5\) storey'
    AND description ~ 'dwelling|residential'
    UNION
    SELECT id, description, lat, lng, lga_fullname, 6 as storey
    FROM planning_application
    WHERE description ~ 'apartment'
    AND description ~ 'dwelling|residential';
    UNION
    CREATE VIEW four_storeys AS
    SELECT id, description, lat, lng, lga_fullname, 4 as storey
    FROM planning_application
    WHERE description ~ 'four storey|4\) storey'
    AND description ~ 'dwelling|residential';
    ''',
        '''
    CREATE VIEW dwellings as SELECT lga_code_2021, (
	opds_separate_house_dwellings +
	opds_sd_r_t_h_th_1_sty_dwgs +
	opds_flt_apt_att_house_ds
) as "Single Storey Total",
from vic_selected_census;

    ''',
    '''
    CREATE VIEW dwellings as SELECT lga_code_2021, (
	opds_sd_r_t_h_th_2_m_sty_dwgs
	opds_f_ap_i_1or2_sty_blk_ds
) as "Two Storey Total",
from vic_selected_census;

    ''',
     '''
    CREATE VIEW dwellings as SELECT lga_code_2021, (
	opds_f_ap_i_3_sty_blk_dwgs
	opds_f_ap_i_1or2_sty_blk_ds
) as "Three Storey Total",
from vic_selected_census;

    ''',
         '''
    CREATE VIEW dwellings as SELECT lga_code_2021, (
	opds_f_ap_i_4to8_sty_blk_ds
	opds_f_ap_i_9_m_sty_blk_ds
) as "Four Storey and Above Storey Total",
from vic_selected_census;
'''
    ''',
    CREATE VIEW dwellings as SELECT lga_code_2021, (
	opds_separate_house_people +
	opds_sd_r_t_h_th_1_sty_psns +
	opds_flt_apt_att_house_ps
) as "Single Storey People Total",
from vic_selected_census;

    ''',
    '''
    CREATE VIEW dwellings as SELECT lga_code_2021, (
	opds_sd_r_t_h_th_2_m_sty_psns
	opds_f_ap_i_1or2_sty_blk_ps
) as "Two Storey Total",
from vic_selected_census;

    ''',
     '''
    CREATE VIEW dwellings as SELECT lga_code_2021, (
	opds_f_ap_i_3_sty_blk_psns
	opds_f_ap_i_1or2_sty_blk_ps
) as "Three Storey Total",
from vic_selected_census;

    ''',
         '''
    CREATE VIEW dwellings as SELECT lga_code_2021, (
	opds_f_ap_i_4to8_sty_blk_ps
	opds_f_ap_i_9_m_sty_blk_ps
) as "Four Storey and Above Storey Total",
from vic_selected_census;

    ''',
    '''
    CREATE VIEW all_storey AS
    SELECT id, description, lat, lng, lga_fullname, storey
    FROM double_storeys
    UNION
    SELECT id, description, lat, lng, lga_fullname, storey
    FROM three_storeys
    UNION
    SELECT id, description, lat, lng, lga_fullname, storey
    FROM four_storeys
    UNION
    SELECT id, description, lat, lng, lga_fullname, storey
    FROM five_storeys
    UNION
    SELECT id, description, lat, lng, lga_fullname, storey
    FROM apartments;
    '''


    ]

    for query in query_list: execute_sql(query)