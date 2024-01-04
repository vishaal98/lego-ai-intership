# Create an instance of the DatabaseSingleton
from singletonClass import Database

db = Database()

# Establish a connection to the database
connection = db.get_connection(
    dbname='lego_ai',
    user='postgres',
    password='password',
    host='127.0.0.1',
    port='5433'
)

# Example: Fetch data
fetch_query = "SELECT * FROM table1;"
json_data = db.fetch(fetch_query)
print(json_data)

# Example: Execute query
example_query = "UPDATE table1 SET size = 'lg'  WHERE size='l';"

affected_rows = db.execute(example_query)
print(f"Affected rows: {affected_rows}")
