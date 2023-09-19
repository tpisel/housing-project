# create tables and views in the database for querying

from sqlalchemy import create_engine, text


def run_ctas(engine):

    def execute_sql(query):
            with engine.connect() as connection:
                result = connection.execute(text(query))

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
    '''
    '''
    CREATE VIEW four_storeys AS
    SELECT id, description, lat, lng, lga_fullname, 4 as storey
    FROM planning_application
    WHERE description ~ 'four storey|4\) storey'
    AND description ~ 'dwelling|residential';
    ''',
    '''
    CREATE VIEW five_storeys AS
    SELECT id, description, lat, lng, lga_fullname, 5 as storey
    FROM planning_application
    WHERE description ~ 'five storey|5\) storey'
    AND description ~ 'dwelling|residential';
    ''',
    '''
    CREATE VIEW apartments AS
    SELECT id, description, lat, lng, lga_fullname, 6 as storey
    FROM planning_application
    WHERE description ~ 'apartment'
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