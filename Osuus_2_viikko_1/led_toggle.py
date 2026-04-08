from time import sleep

import RPi.GPIO as GPIO

PIN_NAPPI = 12
PIN_LED = 11


def nappi_painettu(_):
    status = not GPIO.input(PIN_LED)
    GPIO.output(PIN_LED,status)
    print("LED päällä" if status else "LED pois")


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_NAPPI,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_LED,GPIO.OUT)
    GPIO.add_event_detect(PIN_NAPPI, GPIO.FALLING, callback=nappi_painettu, bouncetime=50)

    try:
        while True:
            sleep(0.1)

    except KeyboardInterrupt:
        print("\ninterrupted.")
    finally:
        GPIO.cleanup()



if __name__ == "__main__":
    main()
