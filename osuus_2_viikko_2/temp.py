import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

TEMP = '/sys/bus/w1/devices/28-3c01f0963f1a/w1_slave'


def temp_raw():
    f = open(TEMP, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = temp_raw()

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()

    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    
        
def main():
    while True:
        print(f"{read_temp()}°C")
        time.sleep(1)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted")