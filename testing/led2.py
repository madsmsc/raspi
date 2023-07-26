from time import sleep
from threading import Thread
try:
    import RPi.GPIO as GPIO
except:    
    print('couldn\'t load RPi - probably not running on raspi')

keepGoing = False

ledPins = [12, 16]
curPin = 0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPins[0], GPIO.OUT)
GPIO.setup(ledPins[1], GPIO.OUT)

def pin():
    return ledPins[curPin]

while(True):
    GPIO.output(pin(), GPIO.HIGH)
    curPin = (curPin + 1) % 2
    GPIO.output(pin(), GPIO.LOW)
    sleep(1)

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
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)    
    try:
        while keepGoing:
            runBlinkLoop()
    except KeyboardInterrupt:
        print('quit!')
        GPIO.cleanup()

def runBlinkLoop():
    GPIO.output(17, GPIO.LOW) # red off
    GPIO.output(27, GPIO.HIGH) # blue on
    sleep(0.5)
    GPIO.output(27, GPIO.LOW) # blue off
    GPIO.output(17, GPIO.HIGH) # red on
    GPIO.cleanup()
    sleep(0.5)            

def on():
    print('led on')
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)

def off():
    print('led off')
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
