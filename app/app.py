from flask import Flask, render_template, request
import psycopg2
import os
from dotenv import load_dotenv,find_dotenv

app = Flask(__name__)

load_dotenv(find_dotenv("../.env"))

DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.getenv('DB_PORT')
DB_NAME = 5432

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# PostgreSQL connection details (replace with your actual credentials)
#DATABASE_URL = "postgres://postgres:postgres@db:5432/test"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']

    try:
        # Connect to the PostgreSQL database
        #conn = psycopg2.connect(DATABASE_URL)
        conn = psycopg2.connect(
            host=os.environ.get("POSTGRES_HOST"),
            database=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
        )
        cur = conn.cursor()

        # Insert data into the existing table
        cur.execute("INSERT INTO us (username, email) VALUES (%s, %s)", (username, email))
        conn.commit()

        cur.execute("""SELECT * FROM us""")
        result1 = cur.fetchall()
        for r in result1:
            print(r)

        cur.close()
        conn.close()

        return f"Data inserted successfully!{result1}"

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return "Failed to insert data."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
