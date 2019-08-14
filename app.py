from flask import Flask, render_template, redirect, url_for
import json, datetime, requests

app = Flask(__name__)
#IP = 'http://192.168.87.105'
IP = 'http://localhost'
API_LED = IP + ':5001'
API_CHART = IP + ':5002'
API_OS = IP + ':5003'

@app.route('/on')
def routeOn():
    res = requests.get(API_LED + '/on')
    print('res=' + res.text)

@app.route('/off')
def routeOff():
    res = requests.get(API_LED + '/off')
    print('res=' + res.text)

@app.route('/blinkOn')
def routeBlinkOn():
    res = requests.get(API_LED + '/blinkOn')
    print('res=' + res.text)

@app.route('/blinkOff')
def routeBlinkOff():
    res = requests.get(API_LED + '/blinkOff')
    print('res=' + res.text)

@app.route('/temp')
def routeTemp():
    res = requests.get(API_CHART + '/temp')
    res = json.loads(res.text)
    return render_template('chart.html', **res);

@app.route("/light")
def routeChart():
    res = requests.get(API_CHART + '/light')
    res = json.loads(res.text)
    return render_template('chart.html', **res)
            
@app.route('/cam')
def routeCam():
    return render_template('cam.html')

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('pageNotFound.html'), 404

@app.route('/services')
@app.route('/index')
@app.route('/')
def index():
    temp = requests.get(API_CHART + '/tempNow').text
    light = requests.get(API_CHART + '/lightNow').text
    ser = requests.get(API_OS + '/services').text
    params = {'c': json.loads(temp)['v'],
              'lm': json.loads(light)['v'],
              'ser': json.loads(ser)}
    return render_template('index.html', **params)

@app.route('/clock')
def routeClock():
    return render_template('clock.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

