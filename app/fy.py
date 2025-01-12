import os
from dotenv import load_dotenv,find_dotenv

#"../.env"
load_dotenv(find_dotenv())
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
print(DB_USER)