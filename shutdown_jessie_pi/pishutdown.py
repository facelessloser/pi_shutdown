# shutdown/reboot(/power on) Raspberry Pi with pushbutton

import RPi.GPIO as GPIO
from subprocess import call
import time

shutdownPin = 15 


GPIO.setmode(GPIO.BOARD)
GPIO.setup(shutdownPin, GPIO.IN)
GPIO.setup(16, GPIO.OUT) # Set up pin 16 as an output

def buttonStateChanged(pin):

    if not (GPIO.input(pin)):
        #print"button press"
        GPIO.output(16, True) # Turn on pin 16 (LED)
        #print"Shutdown"
        call(['shutdown', '-h', 'now'], shell=False)

GPIO.add_event_detect(shutdownPin, GPIO.BOTH, callback=buttonStateChanged)

while True:
    # sleep to reduce unnecessary CPU usage
    time.sleep(5)
