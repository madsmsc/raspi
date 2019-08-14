from flask import Flask, render_template, redirect, url_for, jsonify
from time import sleep
from threading import Thread
try:
    import RPi.GPIO as GPIO
except:    
    print('couldn\'t load RPi - probably not running on raspi')

app = Flask(__name__)
keepGoing = False

@app.route('/blinkOff')
def routeBlinkOff():
    print('blink: stop')
    global keepGoing
    keepGoing = False
    return jsonify('OK')

@app.route('/blinkOn')
def routeBlinkOn():
    print('blink: run')
    global keepGoing
    keepGoing = True
    t = Thread(target=runBlink)
    t.start()
    return jsonify('OK')

def runBlink():
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
        print('quit!')
        GPIO.cleanup()

@app.route('/on')
def routeOn():
    print('led on')
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    return jsonify('OK')

@app.route('/off')
def routeOff():
    print('led off')
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    return jsonify('OK')

@app.errorhandler(404)
def pageNotFound(error):
    return jsonify('FAIL')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

