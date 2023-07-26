from time import sleep
from threading import Thread
try:
    import RPi.GPIO as GPIO
except:    
    print('couldn\'t load RPi - probably not running on raspi')

keepGoing = False
ledPins = [12, 16]
curPin = 0

def pin():
    return ledPins[curPin]

def nextPin():
    global curPin
    curPin = (curPin + 1) % 2
    return pin()

def blinkOff():
    print('blink: stop')
    global keepGoing
    keepGoing = False

def blinkOn():
    print('blink: run')
    global keepGoing
    keepGoing = True
    t = Thread(target=runBlink)
    t.start()

def runBlink():
    global keepGoing
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin(), GPIO.OUT)
    GPIO.setup(nextPin(), GPIO.OUT)
    try:
        while keepGoing:
            runBlinkLoop()
    except KeyboardInterrupt:
        print('quit!')
        #GPIO.cleanup()

def runBlinkLoop():
    GPIO.output(pin(), GPIO.HIGH)
    GPIO.output(nextPin(), GPIO.LOW)
    #GPIO.cleanup()
    sleep(0.5)
    
def on():
    print('led on')
    #GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin(), GPIO.OUT)
    GPIO.setup(nextPin(), GPIO.OUT)
    GPIO.output(pin(), GPIO.HIGH)
    GPIO.output(nextPin(), GPIO.HIGH)
    
def off():
    print('led off')
    #GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin(), GPIO.OUT)
    GPIO.setup(nextPin(), GPIO.OUT)
    GPIO.output(pin(), GPIO.LOW)
    GPIO.output(nextPin(), GPIO.LOW)
