import sys
import json
import time

import RPi.GPIO as GPIO

PIN = 11

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN,GPIO.OUT)
    while True:
        try:
            lkm = int(input("Monta kertaa vilkutetaan?"))
            pass
        except ValueError:
            print("Syötä kokonaisluku")

            try:
                for i in range(lkm):
                    print(f"kierros {i + 1}")
                    GPIO.output(PIN,1)
                    time.sleep(1)
                    GPIO.output(PIN,0)
                    time.sleep(1)

                print("loop ohitettu")
                
            except KeyboardInterrupt:
                print("\ninterrupted")
                break
            finally:
                GPIO.cleanup()

if __name__ == "__main__":
    main()
