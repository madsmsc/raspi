import os
import datetime
from time import sleep
import RPi.GPIO as GPIO

DB_FILE = "light_db.txt"
TIME_FORMAT = "%Y-%m-%d %H:%M"

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
        f = open(DB_FILE, "a+")
        GPIO.setmode(GPIO.BCM)
        LDRReading = RCtime(3)
        t = RCtime(3)
        GPIO.cleanup()
        now = datetime.datetime.now()
        d = now.strftime(TIME_FORMAT)
        s = '{"v":"' + str(t)
        s += '", "d":"' + d + '"}'
        f.write(s)
        f.close()
        sleep(4000)#60*30)
