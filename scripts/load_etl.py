import psycopg2
from psycopg2 import sql
import os
from pathlib import Path
from dotenv import load_dotenv 

# --- CONFIGURATION ---
load_dotenv()  # Load environment variables from .env
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DATA_DIR = Path("data/data_clean")
SCHEMA_FILE = Path("sql/schema.sql")

# --- TABLE TO FILE MAPPING (ORDERED BY DEPENDENCIES) ---
table_files = [
    ("neighbourhood_groups", "neighbourhood_groups.csv"),
    ("neighbourhoods", "neighbourhoods.csv"),
    ("room_types", "room_types.csv"),
    ("hosts", "hosts.csv"),
    ("listings", "listings.csv"),
    ("reviews", "reviews.csv"),
]

# --- MAIN ETL LOGIC ---
def run_etl():
    try:
        print("Connecting to PostgreSQL...")
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Step 1: Run schema.sql to create tables
        print("Creating schema...")
        with open(SCHEMA_FILE, "r") as f:
            cur.execute(f.read())

        # Step 2: Load data into tables
        for table, csv_file in table_files:
            file_path = DATA_DIR / csv_file
            print(f"Loading {file_path} into {table}...")
            with open(file_path, "r", encoding="utf-8") as f:
                next(f)  # Skip header
                cur.copy_expert(sql.SQL("""
                    COPY {} FROM STDIN WITH CSV HEADER DELIMITER ',' NULL '';
                """).format(sql.Identifier(table)), f)

        print("✅ ETL completed successfully.")

    except Exception as e:
        print(f"❌ Error during ETL: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    run_etl()
