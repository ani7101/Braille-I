import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(11) == False :
        print("The button is pressed")
    time.sleep(0.2)
