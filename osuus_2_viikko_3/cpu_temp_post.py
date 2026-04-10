import sys
from time import sleep
import urllib.request
import os
import random

from dotenv import load_dotenv

load_dotenv("../.env")

WRITE = os.getenv("WRITE_API_KEY")
URL = f'https://api.thingspeak.com/update?api_key={WRITE}&field1='

def main():
    while True:
        with open('/sys/class/thermal/thermal_zone0/temp') as temp:
            temp = int(temp.read()) / 1e3

        print(temp)

        with urllib.request.urlopen(URL + str(temp)) as conn:
            conn.read()

        sleep(15)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted")
