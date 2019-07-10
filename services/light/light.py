import os
import datetime
from time import sleep
import RPi.GPIO as GPIO

def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    sleep(0.1)
    GPIO.setup(RCpin, GPIO.IN)
    while(GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

def run():
    while(True):
        f = open("db.txt", "a+")
        GPIO.setmode(GPIO.BCM)
        LDRReading = RCtime(3)
        t = RCtime(3)
        GPIO.cleanup()
        d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        s = '{"v":"' + str(t) + '", "d":"' + d + '"}'
        f.write(s)
        f.close()
        sleep(60*30)
        
run()
