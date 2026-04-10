from time import sleep
import os

from dotenv import load_dotenv
import psutil
import requests

load_dotenv()

WRITE = os.getenv("WRITE_API_KEY")
URL = f'https://api.thingspeak.com/update?api_key={WRITE}&'
FIELDS = {
    "cpu":"field4",
    "ram":"field3"
}


def main():
    counter = 0
    
    while True:
        post = " POST" if not counter % 8 else ""
        stats = {
        "cpu":psutil.cpu_percent(),
        "ram":psutil.virtual_memory().percent
        }
        
        if post:
            params = "&".join(f"{field}={stats[key]}" for key, field in FIELDS.items())
            requests.post(f"{URL}{params}")
            print(f"cpu: {stats['cpu']:>5.2f}% ram: {stats['ram']:>5.2f}%")

        counter += 1
        sleep(2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted")