from urllib import request
from dotenv import load_dotenv
import os

load_dotenv()

READ = os.getenv("READ_API_KEY")
URL = f"https://api.thingspeak.com/channels/3322534/feeds.json?api_key={READ}"  

def main():
    with request.urlopen(URL) as conn:
        print(conn.read())


if __name__ == "__main__":
    main()