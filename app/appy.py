import psycopg2
import os
import time
def val(i):
    try:
        conn = psycopg2.connect(
            host=os.environ.get("POSTGRES_HOST"),
            database=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
        )
        cur = conn.cursor()
        k=f'user{i}@example.com'
        cur.execute("INSERT INTO us (username, email) VALUES ('user1', %s)",(k,))  # Very simple query
        #result = cur.fetchone()
        result = conn.commit()
        print(f"Database connected and query executed: {result}")
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"General error: {e}")

if __name__ == '__main__':
#while True:
    for i in range(103,200):
        time.sleep(10)
        val(i)
        print("App finished.") # Indicate normal exit