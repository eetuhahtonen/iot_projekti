from time import sleep

from db import db_commit, db_init
from thingspeak import get_last, get_all
from dotenv import load_dotenv, dotenv_values

load_dotenv()

LAST_ID = dotenv_values(".env").get("LAST_ID")

def main():    
    conn = db_init()

    try:
        
        if LAST_ID is None:
            db_commit(get_all(), conn)
            print("Added all old entries to database.")

        while True:
            if data := get_last():
                db_commit(data, conn)
                print("Entry added to database")

            sleep(2)
    
    finally:
        conn.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted")