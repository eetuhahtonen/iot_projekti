from time import sleep
import RPi.GPIO as GPIO

pin_nappi = 12
pin_led = 11


def nappi_painettu(_):
    status = not GPIO.input(pin_led)
    GPIO.output(pin_led,status)
    print("LED päällä" if status else "LED pois")


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_nappi,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pin_led,GPIO.OUT)
    GPIO.add_event_detect(pin_nappi, GPIO.FALLING, callback=nappi_painettu, bouncetime=50)
    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        print("\ninterrupted.")
    finally:
        GPIO.cleanup()



if __name__ == "__main__":
    main()
