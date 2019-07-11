from flask import Flask, render_template, redirect, url_for
from urllib.request import urlopen
import os, json, datetime

app = Flask(__name__)
IP = 'http://192.168.87.105:'

@app.route('/on')
def routeOn():
    print('led on')
    with urlopen(IP + '5001/on') as r:
        res = r.read()
    print('res=' + res)

@app.route('/off')
def routeOff():
    print('led off')
    with urlopen(IP + '5001/off') as r:
        res = r.read()
    print('res=' + res)

@app.route('/blinkOn')
def routeBlinkOn():
    print('led blink on')
    with urlopen(IP + '5001/off') as r:
        res = r.read()
    print('res=' + res)

@app.route('/blinkOff')
def routeBlinkOff():
    print('led blink off')
    with urlopen(IP + '5001/off') as r:
        res = r.read()
    print('res=' + res)

@app.route('/temp/')
def routeTemp():
    print('get temp')
    with urlopen(IP + '5002/temp') as r:
        res = r.read()    
    params = res
    """{'values': readTempDB(),
              'header': 'temp',
              'stepSize': 1,
              'chartMin': 20,
              'chartMax': 30,
              'time': timeString() } 
    """
    return render_template('chart.html', **params);

@app.route("/light/")
def routeChart():
    print('get light')
    with urlopen(IP + '5002/temp') as r:
        res = r.read()
    params = res
    """
    params = {'values': readLightDB(),
              'header': 'light',
              'stepSize': 5,
              'chartMin': 120,
              'chartMax': 130,
              'time': timeString() }
    """
    return render_template('chart.html', **params)

def timeString():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            
@app.route('/cam/')
def routeCam():
    print('get cam')
    return render_template('cam.html')

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('pageNotFound.html'), 404

@app.route('/index')
@app.route('/')
def index():
    with urlopen(IP + '5002/tempNow') as r:
        temp = r.read()
    with urlopen(IP + '5002/lightNow') as r:
        light = r.read()
    with urlopen(IP + '5003/services') as r:
        ser = r.read()
    params = {'c': temp,
              'lm': light,
              'ser': ser,
              'time': timeString() }
    return render_template('index.html', **params)

@app.route('/clock')
def routeClock():
    return render_template('clock.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

