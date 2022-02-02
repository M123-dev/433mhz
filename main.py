import RPi.GPIO as GPIO
import time


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.IN)
    while True:
        if GPIO.input(13) == 0:
            print("0")
        else:
            print("1")
        time.sleep(3)


if __name__ == '__main__':
    main()
