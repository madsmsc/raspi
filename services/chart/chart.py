from flask import Flask, render_template, redirect, url_for, jsonify
import json, datetime

app = Flask(__name__)

def timeString():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def readTempDB():
    return string2json('services/temp/db.txt')

def readLightDB():
    return string2json('services/light/db.txt')

def string2json(filename):
    f = open(filename, "r")
    s = '['
    ## TEST
    #d = datetime.datetime.now().strftime('%Y-%m-%d')
    d = '2019-07-07 00:00'
    for line in f.readlines():
        if d in line:
            s += line.replace('\n', '')
    s = s.replace('}', '},')
    if len(s) > 5:
        s = s[:-1]
    s += ']'
    f.close()
    j = json.loads(s)
    return j

def tempParams():
    return {'values': readTempDB(),
            'header': 'temp',
            'stepSize': 1,
            'chartMin': 20,
            'chartMax': 30,
            'time': timeString() }

def lightParams():
    return {'values': readLightDB(),
            'header': 'light',
            'stepSize': 5,
            'chartMin': 120,
            'chartMax': 130,
            'time': timeString() }

@app.route('/temp')
def routeTemp():
    print('/temp')
    return jsonify(tempParams())

@app.route("/light")
def routeLight():
    print('/light')
    return jsonify(lightParams())

@app.route("/lightNow")
def routeLightNow():
    print('/lightNow')
    return jsonify(readLightDB()[0])

@app.route("/tempNow")
def routeTempNow():
    print('/tempNow')
    return jsonify(readTempDB()[0])

# fix some way of seeing other weeks, seeing months, years, etc.

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
