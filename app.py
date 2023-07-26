from flask import Flask, render_template, redirect, url_for, jsonify
import datetime, requests
# my modules
import led, chart, temp, light, ir, oss

#ir.run() # not ready yet
#light.run()
#temp.run()
# do these as threads?
# look at the other .py that uses threads
# probably light/time/temp/etc.

app = Flask(__name__)
#IP = 'http://192.168.87.105'
IP = 'http://localhost'

def renderIndex():
    p = {'c': chart.tempNow()['v'],
         'lm': chart.lightNow()['v'],
         'ser': oss.services(),
         'uptime': oss.uptime()}
    return render_template('index.html', **p)    

@app.route('/on')
def routeOn():
    led.on()
    return renderIndex()

@app.route('/off')
def routeOff():
    led.off()
    return renderIndex()

@app.route('/blinkOn')
def routeBlinkOn():
    led.blinkOn()
    return renderIndex()

@app.route('/blinkOff')
def routeBlinkOff():
    led.blinkOff()
    return renderIndex()

@app.route('/temp')
def routeTemp():
    p = chart.tempParams()
    return render_template('chart.html', **p)

@app.route("/light")
def routeChart():
    p = chart.lightParams()
    return render_template('chart.html', **p)
            
@app.route('/cam')
def routeCam():
    return render_template('cam.html')

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('pageNotFound.html'), 404

@app.route('/index')
@app.route('/')
def index():
    return renderIndex()
    
@app.route('/clock')
def routeClock():
    return render_template('clock.html')

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)
