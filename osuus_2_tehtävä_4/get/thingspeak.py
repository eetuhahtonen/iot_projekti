import os

import requests
from dotenv import load_dotenv, set_key, dotenv_values

load_dotenv()

ID = os.getenv("CHANNEL_ID")
READ = os.getenv("WRITE_API_KEY")


def get_last():
    URL = f"https://api.thingspeak.com/channels/{ID}/feeds/last.json?api_key={READ}"
    last_id = dotenv_values(".env").get("LAST_ID")
    data = []
    _data = requests.get(URL).json()

    try:
        if _data['created_at'] == last_id:
            return
        
        if _data["field3"]:
            d = {
            "created_at":_data['created_at'].replace("T"," ").replace("Z",""),
            "sensor":"ram_use",
            "value":float(_data['field3']),
            "unit":"%"
            }
            data.append(d)

        if _data["field4"]:
            d = {
            "created_at":_data['created_at'].replace("T"," ").replace("Z",""),
            "sensor":"cpu_use",
            "value":float(_data['field4']),
            "unit":"%"
            }
            data.append(d)

        set_key(".env", "LAST_ID", _data["created_at"])
        return data
            
    except (ValueError, TypeError):
        print(f"Virheellinen data!{_data}")


def get_all():
    URL = f"https://api.thingspeak.com/channels/{ID}/feeds.json?api_key={READ}"
    data = []
    _data = requests.get(URL).json()

    for row in _data['feeds']:
        try:

            if row["field3"]:
                d = {
                "created_at":row['created_at'].replace("T"," ").replace("Z",""),
                "sensor":"ram_use",
                "value":float(row['field3']),
                "unit":"%"
                }
                data.append(d)

            if row["field4"]:
                d = {
                "created_at":row['created_at'].replace("T"," ").replace("Z",""),
                "sensor":"cpu_use",
                "value":float(row['field4']),
                "unit":"%"
                }
                data.append(d)

        except (ValueError, TypeError):
            print(f"Virheellinen data!{row}")

    if data:
        set_key(".env", "LAST_ID", _data['feeds'][-1]["created_at"])
        return data

