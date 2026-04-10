import os

import mariadb
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_DATABASE")


def db_commit(data,conn):
    cur = conn.cursor()

    for row in data:
        cur.execute(
            "INSERT INTO mac_use (time_stamp, sensor, value, unit) VALUES (?, ?, ?, ?)",
            (row["created_at"], row["sensor"], row["value"], row["unit"])
            )
        
    conn.commit()


def db_init():
    conn = mariadb.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DATABASE
        )
    return conn