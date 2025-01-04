from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# PostgreSQL connection details (replace with your actual credentials)
DATABASE_URL = "postgres://postgres:postgres@db:5432/test"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        # Insert data into the existing table
        cur.execute("INSERT INTO us (username, email) VALUES (%s, %s)", (username, email))
        conn.commit()

        cur.close()
        conn.close()

        return "Data inserted successfully!"

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return "Failed to insert data."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
