import RPi.GPIO as GPIO
from time import sleep

# i should really use double-quotes?
# or single quotes?

GPIO_PIR = 7

curState = 0
prevState = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.OUT)
    print("PIR module test (CTRL-C to exit)")
    GPIO.setup(GPIO_PIR, GPIO.IN)

def irLoop():
    # isn't a global missing here?
    curState = GPIO.input(GPIO_PIR)
    if curState == 1 and prevState == 0:
        print(" motion detected!")
        # persist in some ir_db.txt ?
        # with some timestamps
        # like the other dbs
        # so I can see history...
        GPIO.output(27, GPIO.HIGH)
        sleep(1)
        GPIO.output(27, GPIO.LOW)
        prevState = 1
    elif curState == 0 and prevState == 1:
        print(" ready!")
        prevState = 0
        sleep(0.01)
    
def run():
    try:
        print("waiting for PIR to settle")
        while GPIO.input(GPIO_PIR) == 1:
            curState = 0
            # this probably isn't needed
            print(" ready!")
        while True:
            irLoop()
    except KeyboardInterrupt:
        print(" quit!")
        GPIO.cleanup()
