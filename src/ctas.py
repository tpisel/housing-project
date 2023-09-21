# create tables and views in the database for querying

from sqlalchemy import create_engine, text


def run_ctas(engine):

    query_list = '''

    CREATE VIEW vic_selected_census AS
    SELECT * -- this bit can be edited to create simple transformed columns
    FROM local_gov_area
        LEFT JOIN dwellings_by_bedroom USING (lga_code_2021)
        LEFT JOIN dwelling_structure USING (lga_code_2021)
        LEFT JOIN selected_medians USING (lga_code_2021)
        LEFT JOIN vehicles_per_dwelling USING (lga_code_2021)
    WHERE LEFT(lga_code_2021, 4) = 'LGA2';

    CREATE VIEW double_storeys AS
    SELECT id, description, lat, lng, lga_fullname, 2 as storey
    FROM planning_application
    WHERE description ~ 'double storey|two storey|2\) storey'
    AND description ~ 'dwelling|residential';

    CREATE VIEW three_storeys AS
    SELECT id, description, lat, lng, lga_fullname, 3 as storey
    FROM planning_application
    WHERE description ~ 'triple storey|three storey|3\) storey'
    AND description ~ 'dwelling|residential';

    CREATE VIEW single_storey AS
    SELECT id, description, lat, lng, lga_fullname, 1 as storey
    FROM planning_application
    WHERE description ~ 'single storey|one storey|1\) storey'
    AND description ~ 'dwelling|residential'
    AND description ~ 'development';

    CREATE VIEW combined_view AS
    SELECT id, description, lat, lng, lga_fullname, 5 as storey
    FROM planning_application
    WHERE description ~ 'five storey|5\) storey'
    AND description ~ 'dwelling|residential'
    UNION
    SELECT id, description, lat, lng, lga_fullname, 6 as storey
    FROM planning_application
    WHERE description ~ 'apartment'
    AND description ~ 'dwelling|residential'
    UNION
    SELECT id, description, lat, lng, lga_fullname, 4 as storey
    FROM planning_application
    WHERE description ~ 'four storey|4\) storey'
    AND description ~ 'dwelling|residential';

    CREATE VIEW all_storey AS
    SELECT id, description, lat, lng, lga_fullname, 1 AS storey
    FROM planning_application
    WHERE description ~ 'single storey|one storey|1\) storey'
    AND description ~ 'dwelling|residential'
    AND description ~ 'development'
    UNION
    SELECT id, description, lat, lng, lga_fullname, 2 AS storey
    FROM planning_application
    WHERE description ~ 'double storey|two storey|2\) storey'
    AND description ~ 'dwelling|residential'
    UNION
    SELECT id, description, lat, lng, lga_fullname, 3 AS storey
    FROM planning_application
    WHERE description ~ 'triple storey|three storey|3\) storey'
    AND description ~ 'dwelling|residential'
    UNION
    SELECT id, description, lat, lng, lga_fullname, 4 AS storey
    FROM planning_application
    WHERE description ~ 'four storey|4\) storey'
    AND description ~ 'dwelling|residential'
    UNION
    SELECT id, description, lat, lng, lga_fullname, 5 AS storey
    FROM planning_application
    WHERE description ~ 'five storey|5\) storey'
    AND description ~ 'dwelling|residential'
    UNION
    SELECT id, description, lat, lng, lga_fullname, 6 AS storey
    FROM planning_application
    WHERE description ~ 'apartment'
    AND description ~ 'dwelling|residential';

    CREATE VIEW dwellings AS
    SELECT lga_code_2021,
        (
                opds_separate_house_dwellings +
                opds_sd_r_t_h_th_1_sty_dwgs +
                opds_flt_apt_att_house_ds
            ) AS "Single Storey Total",
        (
                opds_sd_r_t_h_th_2_m_sty_dwgs +
                opds_f_ap_i_1or2_sty_blk_ds
            ) AS "Two Storey Total",
        (
                opds_f_ap_i_3_sty_blk_dwgs +
                opds_f_ap_i_1or2_sty_blk_ds
            ) AS "Three Storey Total",
        (
                opds_f_ap_i_4to8_sty_blk_ds +
                opds_f_ap_i_9_m_sty_blk_ds
            ) AS "Four Storey and Above Storey Total"
    FROM vic_selected_census;

    '''

    # for query in query_list: execute_sql(query)

    print('running select queries')
    with engine.connect() as connection:
        connection.execute(text(query_list))
        #connection.commit()
    print('select queries run')


if __name__ == "__main__":

    from utils import get_secret
    planning_alerts_key = get_secret('planningalerts')
    pg_password = get_secret('postgres')

    engine = create_engine(f'postgresql://postgres:{pg_password}@localhost:5432/melbournehousingdb')

    run_ctas(engine)
