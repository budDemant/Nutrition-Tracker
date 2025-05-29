import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DBNAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST")
    )

def get_one_row(table_name):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name} LIMIT 1;")
            row = cur.fetchone()
            return row
    finally:
        conn.close()

# Test connection and fetch a row
if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Connection successful!")
        conn.close()
        row = get_one_row("foods")
        print("First row:", row)
    except Exception as e:
        print("Connection failed:")
        print(e)