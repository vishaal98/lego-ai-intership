import psycopg2
import json

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def get_connection(self, dbname, user, password, host, port):
        if self.connection is None:
            try:
                self.connection = psycopg2.connect(
                    dbname=dbname, user=user, password=password, host=host, port=port
                )
                print("Connected to the database")
            except psycopg2.Error as e:
                print(f"Error: Could not connect to the database - {e}")
        return self.connection

    def fetch(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        results = cursor.fetchall()
        cursor.close()

        # Convert results to JSON format
        json_results = []
        for row in results:
            json_results.append(dict(zip(columns, row)))
        return json.dumps(json_results)

    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        affected_rows = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return affected_rows
