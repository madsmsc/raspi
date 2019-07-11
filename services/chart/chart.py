from flask import Flask, render_template, redirect, url_for, jsonify

app = Flask(__name__)

def readTempDB():
    return string2json('services/temp/db.txt')

def readLightDB():
    return string2json('services/light/db.txt')

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
def routeChart():
    print('get light')
    params = {'values': readLightDB(),
              'header': 'light',
              'stepSize': 5,
              'chartMin': 120,
              'chartMax': 130,
              'time': timeString() }
    return jsonify(params)

# fix some way of seeing other weeks, seeing months, years, etc.

if __name__ == '__main__':
    app.run(debug=True, port=5002)
