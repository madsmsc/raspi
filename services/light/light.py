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
        dt = "%Y-%m-%d %H:%M:%S"
        GetDateTime = datetime.datetime.now().strftime(dt)
        LDRReading = RCtime(3)
        t = RCtime(3)
        fo = open("/home/pi/raspi/services/temp.txt", "wb")
        fo.write(GetDateTime)
        LDRReading = str(LDRReading)
        fo.write("\n")
        fo.write(LDRReading)
        fo.close
        GPIO.cleanup()
        f.write(str(t)+'\n')
        f.close()
        sleep(10)

run()
