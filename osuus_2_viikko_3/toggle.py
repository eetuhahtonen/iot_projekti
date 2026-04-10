import urllib.request
import json
import time
import os

from dotenv import load_dotenv  

load_dotenv("../.env")

READ = os.getenv("READ_API_KEY")
ID = os.getenv("CHANNEL_ID")      
URL = f"https://api.thingspeak.com/channels/{ID}/feeds/last.json?api_key={READ}"


def main():
    aikaleima_old = None

    try:
        while True:
            with urllib.request.urlopen(URL) as conn:
                data = json.loads(conn.read())
                print(f"http status code={conn.getcode()}")

            aikaleima = str(data['created_at'])
            userdata = data['field7']

            if aikaleima_old is None:
                print('Skripti startattu, haettu tietokannasta uusin kanavan data')
                print(f'Uusin datapiste: {userdata}')
                aikaleima_old = aikaleima
            elif aikaleima != aikaleima_old:
                print("Uusi arvo tietokannassa")
                print(userdata)
                aikaleima_old = aikaleima

            time.sleep(1)

    except KeyboardInterrupt:   
        print("\ninterrupted")
    finally:
        print("connection lost")


if __name__ == "__main__":
    main()