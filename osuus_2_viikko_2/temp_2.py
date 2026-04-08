import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

TEMP_1 = '/sys/bus/w1/devices/28-3c01f0963f1a/w1_slave'
TEMP_2 = '/sys/bus/w1/devices/28-3c01f096c1af/w1_slave'


def temp_raw(sensor):
    f = open(sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(sensor):
    lines = temp_raw(sensor)

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw(sensor)

    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    
        
def main():
    while True:
        temp1 = read_temp(TEMP_1)
        temp2 = read_temp(TEMP_2)
        temp3 = temp1 + temp2
        print(f"T1: {temp1}°C | T2: {temp2}°C | Tka: {temp3 / 2}°C")
        time.sleep(1)




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted")