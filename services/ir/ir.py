#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

GPIO_PIR = 7
print "PIR module test (CTRL-C to exit)"

GPIO.setup(GPIO_PIR, GPIO.IN)

currentState = 0
previousState = 0

def ir():
    try:
        print "waiting for PIR to settle"
        while GPIO.input(GPIO_PIR) == 1:
            currentState = 0
            print " ready!"
        while True:
            currentState = GPIO.input(GPIO_PIR)
            if currentState == 1 and previousState == 0:
                print " motion detected!"
                GPIO.output(27, GPIO.HIGH)
                sleep(1)
                GPIO.output(27, GPIO.LOW)
                previousState = 1
            elif currentState == 0 and previousState == 1:
                print " ready!"
                previousState = 0
                sleep(0.01)
                    
    except KeyboardInterrupt:
        print " quit!"
        GPIO.cleanup()
        
