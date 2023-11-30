import psycopg2
import requests
import json

# Database connection parameters
DB_NAME = 'postgres'
DB_USER = 'admin'
DB_PASSWORD = '12345'
DB_HOST = 'postgres'  
DB_PORT = '5432'

SQL_SCRIPT_PATH = 'task.sql'

def config_debezium_connector():
    '''
        Set debezium postgres connector with a curl
    '''
    url = "http://connect:8083/connectors/"
    data = {
        "name": "sde-connector",
        "config": {
            "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
            "database.hostname": "postgres",
            "database.port": "5432",
            "database.user": "admin",
            "database.password": "12345",
            "database.dbname": "postgres",
            "database.server.name": "postgres",
            "table.whitelist": "task.transaction",
            "topic.prefix": "task"
        }
    }

    # Headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

 
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if(response.status_code==201):
            print("\nDebezium connector successfully created!\n")
    else:
            print("Debezium Connector Failed!")

def run_sql_script(filename):
    '''
        Connect to the database
        And run the scripts in the file
    '''
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.autocommit = True


    with open(filename, 'r') as file:
        sql_script = file.read()

    cursor = conn.cursor()
    cursor.execute(sql_script)
    cursor.close()


    conn.close()
    print("Your task.sql queries executed successfully.\n")



# Run the script
config_debezium_connector()
run_sql_script(SQL_SCRIPT_PATH)
