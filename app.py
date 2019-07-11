from flask import Flask, render_template, redirect, url_for
import os, json, datetime

NO_SCRIPTS = 'Couldn\'t import scripts - Not running on raspi.'

try:
    from scripts import on, off, blink
except ImportError:
    print(NO_SCRIPTS)

app = Flask(__name__)

@app.route('/on')
def routeOn():
    print('led on')
    try:
        on.run()
    except:
        print(NO_SCRIPTS)
    return redirect(url_for('index'))

@app.route('/off')
def routeOff():
    print('led off')
    try:
        off.run()
    except:
        print(NO_SCRIPTS)
    return redirect(url_for('index'))

@app.route('/blinkOn')
def routeBlinkOn():
    print('led blink on')
    try:
        blink.run()
    except:
        print(NO_SCRIPTS)
    return redirect(url_for('index'))

@app.route('/blinkOff')
def routeBlinkOff():
    print('led blink off')
    try:
        blink.stop()
    except:
        print(NO_SCRIPTS)
    return redirect(url_for('index'))

@app.route('/temp/')
def routeTemp():
    print('get temp')
    params = {'values': readTempDB(),
              'header': 'temp',
              'stepSize': 1,
              'chartMin': 20,
              'chartMax': 30,
              'time': timeString() }
    return render_template('chart.html', **params);

@app.route("/light/")
def routeChart():
    print('get light')
    params = {'values': readLightDB(),
              'header': 'light',
              'stepSize': 5,
              'chartMin': 120,
              'chartMax': 130,
              'time': timeString() }
    return render_template('chart.html', **params)

def timeString():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            
@app.route('/cam/')
def routeCam():
    print('get cam')
    return render_template('cam.html')

@app.route('/services/')
def routeServices():
    print('get services')
    return redirect(url_for('index'))

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
    
def readServices():
    CMD = "ps -Af | grep python"
    """ | cut -d ' ' -f 22 > temp.txt" """
    status = os.system(CMD)
    print('services [status='+str(status)+']')
    s = ''
    skip = ['--color=auto', 'ps', '']
    with open ('services.txt', 'r') as fd:
        for line in fd:
            print('service: '+line)
            if line in skip:
                continue
            s += '[' + line.strip() + '] '
    fd.close();
    return s

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('pageNotFound.html'), 404

@app.route('/index')
@app.route('/')
def index():
    params = {'c': readTempDB()[0]['v'].split('.')[0],
              'lm': readLightDB()[1]['v'].split('.')[0],
              'ser': readServices(),
              'time': timeString() }
    return render_template('index.html', **params)

@app.route('/clock')
def routeClock():
    return render_template('clock.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

