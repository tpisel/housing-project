import keyring
import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine, text
import argparse
import webbrowser

from src.utils import csv_to_table, get_secret
from src.callapi import api_to_db
from src.main import app


def initialise():

    # Request the postgres password and API key
    pg_password = input("\nPlease enter the PostgreSQL password for the 'postgres' user:    (enter for unchanged)\n")
    planning_alerts_key = input("\nPlease enter the API key from PlanningAlerts.org.au:    (enter for unchanged)\n")

    if pg_password:
        keyring.set_password('postgresql', 'postgres', pg_password)
    else:
        pg_password = get_secret('postgres')

    if planning_alerts_key:
        keyring.set_password('planning_alerts', 'api_key', planning_alerts_key)
    else:
        planning_alerts_key = get_secret('planningalerts')

    # create the database if it doesn't exist:
    db_name = 'melbournehousingdb'
    print(f"\nCreating database {db_name}...")

    try:
        conn = psycopg2.connect(dbname='postgres', user='postgres', password=pg_password, host='localhost')
        conn.autocommit = True
        cursor = conn.cursor()

        # Check if the database exists
        cursor.execute(sql.SQL(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'"))
        db_exists = cursor.fetchone()
        
        if db_exists:
            print(f"Database {db_name} already exists!")
            drop = input("\nDo you want to drop and recreate the database? [Y/n]: ")
            if drop.lower() == 'y':
                print(f"\nDropping database {db_name}...")
                cursor.execute(sql.SQL("DROP DATABASE {} WITH (FORCE)").format(sql.Identifier(db_name)))
                print(f"\nCreating database {db_name}...")
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
            else:
                print("Exiting project set up")
                exit(1)
        else:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))

        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        exit(1)

    # upload files to database

    engine = create_engine(f'postgresql://postgres:{pg_password}@localhost:5432/{db_name}')

    print('\n Uploading tables...')
    csv_to_table('./resources/2021_ASGS_Non_ABS_Structures.csv','local_gov_area',engine)
    csv_to_table('./resources/2021Census_G02_VIC_LGA.csv','selected_medians',engine)
    csv_to_table('./resources/2021Census_G34_VIC_LGA.csv','vehicles_per_dwelling',engine)
    csv_to_table('./resources/2021Census_G36_VIC_LGA.csv','dwelling_structure',engine)
    csv_to_table('./resources/2021Census_G41_VIC_LGA.csv','dwellings_by_bedroom',engine)

    # new summary table

    ctas_string = '''
    CREATE TABLE vic_selected_census AS
    SELECT * -- this bit can be edited to create simple transformed columns
    FROM local_gov_area
        LEFT JOIN dwellings_by_bedroom USING (lga_code_2021)
        LEFT JOIN dwelling_structure USING (lga_code_2021)
        LEFT JOIN selected_medians USING (lga_code_2021)
        LEFT JOIN vehicles_per_dwelling USING (lga_code_2021)
    WHERE LEFT(lga_code_2021, 4) = 'LGA2'
    '''

    with engine.connect() as connection:
        result = connection.execute(text(ctas_string))
        connection.commit()

    # download from api
    api_to_db()

    # start app
    start_app()
    
def start_app():
    app.run()
    webbrowser.open('http://127.0.0.1:5000/')
    webbrowser.open('index.html')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Initialise the database.')
    parser.add_argument('--createdb', action='store_true', help='Create the database.')

    args = parser.parse_args()

    if args.createdb:
        initialise()
    else:
        start_app()
