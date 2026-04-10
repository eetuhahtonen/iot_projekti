import urllib.request
import os
import time
import json

import RPi.GPIO as GPIO
from dotenv import load_dotenv

load_dotenv("../.env")

PIN = 11
READ = os.getenv("READ_API_KEY")
ID = os.getenv("CHANNEL_ID")
URL = f"https://api.thingspeak.com/channels/{ID}/feeds/last.json?api_key={READ}"


def toggle(s):
    tila = "päällä" if s else "pois"
    print(f"LED {tila}")
    GPIO.output(PIN, s)


def main():
    edellinen = None
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN,GPIO.OUT)

    try:
        while True:
            with urllib.request.urlopen(URL) as conn:
                data = json.loads(conn.read())
                print(f"http status code={conn.getcode()}")

            if (ohjaus := int(data['field7'])) != edellinen:
                toggle(ohjaus)
                edellinen = ohjaus

            time.sleep(1)

    except KeyboardInterrupt:
        print()
    finally:
        GPIO.cleanup()
        print("connection lost")


if __name__ == "__main__":
    main()
