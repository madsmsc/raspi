from flask import Flask, render_template, redirect, url_for, jsonify

app = Flask(__name__)

def timeString():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def readTempDB():
    return string2json('../temp/db.txt')

def readLightDB():
    return string2json('../light/db.txt')

def string2json(filename):
    f = open(filename, "r")
    s = '['
    d = datetime.datetime.now().strftime('%Y-%m-%d')
    for line in f.readlines():
        if d in line:
            s += line.replace('\n', '')
    s = s.replace('}', '},')
    if len(s) > 5:
        s = s[:-1]
    s += ']'
    print('JSON: '+s)
    f.close()
    j = json.loads(s)
    return j

@app.route('/temp')
def routeTemp():
    print('get temp')
    params = {'values': readTempDB(),
              'header': 'temp',
              'stepSize': 1,
              'chartMin': 20,
              'chartMax': 30,
              'time': timeString() }
    return jsonify(params)

@app.route("/light")
def routeLight():
    print('get light')
    params = {'values': readLightDB(),
              'header': 'light',
              'stepSize': 5,
              'chartMin': 120,
              'chartMax': 130,
              'time': timeString() }
    return jsonify(params)

@app.route("/lightNow")
def routeLightNow():
    return jsonify(readLightDB()[0])

@app.route("/tempNow")
def routeTempNow():
    return jsonify(readTempDB()[0])

# fix some way of seeing other weeks, seeing months, years, etc.

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
