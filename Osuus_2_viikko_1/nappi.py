from time import sleep
import RPi.GPIO as GPIO

pin1 = 11
pin2 = 12


def nappi_painettu(pin):
    if pin == pin1:
        print("Nappi 1 painettu")
    elif pin == pin2:
        print("Nappi 2 painettu")
        

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pin2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin1, GPIO.FALLING, callback=nappi_painettu, bouncetime=50)
    GPIO.add_event_detect(pin2, GPIO.FALLING, callback=nappi_painettu, bouncetime=50)

    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        print("\ninterrupted")
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()