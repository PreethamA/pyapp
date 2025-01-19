import os
from dotenv import load_dotenv,find_dotenv
import psycopg2
#"../.env"

"""
"POSTGRES_USER=postgres",
			"POSTGRES_PASSWORD=postgres",
			"POSTGRES_HOST=db",
			"POSTGRES_DB=test"
"""
load_dotenv(find_dotenv("../.env"))
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
print(f"where its working {DB_USER}")

try:
    conn = psycopg2.connect(
        host=DB_HOST,  # Or "127.0.0.1"
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    print("Connected to PostgreSQL")

except psycopg2.OperationalError as e:
    print(f"Error connecting to PostgreSQL: {e}")