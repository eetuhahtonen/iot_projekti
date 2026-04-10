from thingspeak import get_all, get_last
from time import sleep
while True:
    result = get_last()
    print(f"DEBUG: {result}")
    sleep(2)
