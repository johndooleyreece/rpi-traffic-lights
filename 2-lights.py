# Setup
import RPi.GPIO as GPIO
import time

# start with BCM
GPIO.setmode(GPIO.BCM)

#some constants
GREEN_LIGHT = 9
AMBER_LIGHT = 10
RED_LIGHT = 11

print("Setting up Pins")
GPIO.setup(GREEN_LIGHT, GPIO.OUT)
GPIO.setup(RED_LIGHT, GPIO.OUT)


try:
    while True:
        print("Looping")
        # do stuff
        GPIO.output(GREEN_LIGHT, GPIO.HIGH)
        time.sleep(10)
        GPIO.output(RED_LIGHT, GPIO.HIGH)
        time.sleep(10)
    
finally:
    GPIO.cleanup()


