import psycopg2

def connect_to_db():
    conn_str = "dbname='test' user='postgres' host='127.0.0.1' port='5432' password='postgres'"
    conn = psycopg2.connect(conn_str)
    return conn

if __name__ == "__main__":
    try:
        conn = connect_to_db()
        print("Connected to database successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)