import os
import time
import RPi.GPIO as GPIO

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_sensor = '/sys/bus/w1/devices/28-3c01f09624c0/w1_slave'
pin = 11


def temp_raw():
    f = open(temp_sensor, 'r')
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
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)
    try:
        while True:
            temp =read_temp()
            if temp >= 25:
                GPIO.output(pin, 1)
                print(f"{temp}°C | LED päällä")
            else:
                GPIO.output(pin, 0)
                print(f"{temp}°C | LED pois")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\ninterrupted")
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()