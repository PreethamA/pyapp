import psycopg2
import os
import time
import datetime as  dtime
from dotenv import load_dotenv,find_dotenv
"""
conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_DB"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            
        
"""

def val(i):
    load_dotenv(find_dotenv("../.env"))
    print("is it working in the function")
    try:
        conn = psycopg2.connect(
            host=os.environ.get("POSTGRES_HOST"),
            database=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
        )
        cur = conn.cursor()
        k = f'user{i}@example.com'
        #cur.execute("INSERT INTO us (username, email) VALUES ('user1', %s)",(k,))  # Very simple query
        print(f"emailid:{k}")
        #result = cur.fetchone()
        #conn.commit()

        cur.execute("""SELECT * FROM us""")
        result1 = cur.fetchall()
        for r in result1:
            print(r)
        #print(f"Database connected and query executed: {result1}")
        #cur.close()
        #conn.close()

    except psycopg2.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"General error: {e}")
   # finally:
  #      if conn:
 #           cur.close()
#            conn.close()
if __name__ == '__main__':

 for i in range(303,500):
    print(dtime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(10)
    val(i)
    print("App finished.") # Indicate normal exit