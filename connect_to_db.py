import psycopg2

def connect_to_db(dbname, user, password, host, port):
    conn_string = f"dbname='{dbname}' user='{user}' password='{password}' host='{host}' port='{port}'"
    conn = psycopg2.connect(conn_string)
    return conn

def execute_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows

# Example usage:
conn = connect_to_db("test", "postgres", "postgres", "localhost", "5432")
rows = execute_query(conn, "SELECT * FROM us")

for row in rows:
    print(row)

conn.close()