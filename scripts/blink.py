import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

def stop():
    print 'blink: stop'
    global keepGoing
    keepGoing = False

def run():
    print 'blink: run'
    global keepGoing
    keepGoing = True
    t = Thread(target=doRun)
    t.start()

def doRun():
    global keepGoing
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    
    try:
        while keepGoing:
            GPIO.output(17, GPIO.LOW) # red off
            GPIO.output(27, GPIO.HIGH) # blue on
            sleep(0.5)
            GPIO.output(27, GPIO.LOW) # blue off
            GPIO.output(17, GPIO.HIGH) # red on
            GPIO.cleanup()
            sleep(0.5)
            
    except KeyboardInterrupt:
        print " quit!"
        GPIO.cleanup()
