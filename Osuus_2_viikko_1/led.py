import sys
import json
import RPi.GPIO as GPIO
import time

pin = 11

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)
    while True:
        try:
            lkm = int(input("Monta kertaa vilkutetaan?"))
            pass
        except ValueError:
            print("Syötä kokonaisluku")

            try:
                for i in range(lkm):
                    print(f"kierros {i + 1}")
                    GPIO.output(pin,1)
                    time.sleep(1)
                    GPIO.output(pin,0)
                    time.sleep(1)
                print("loop ohitettu")
            except KeyboardInterrupt:
                print("\ninterrupted")
                break
            finally:
                GPIO.cleanup()

if __name__ == "__main__":
    main()
