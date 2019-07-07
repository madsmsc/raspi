from flask import Flask, render_template, redirect, url_for
from scripts import on, off, blink
import os

app = Flask(__name__)

param = ""

@app.route('/on')
def routeOn():
    print 'led on'
    on.run()
    return redirect(url_for('index'))

@app.route('/off')
def routeOff():
    print 'led off'
    off.run()
    return redirect(url_for('index'))

@app.route('/blinkOn')
def routeBlinkOn():
    print 'led blink on'
    blink.run()
    return redirect(url_for('index'))

@app.route('/blinkOff')
def routeBlinkOff():
    print 'led blink off'
    blink.stop()
    return redirect(url_for('index'))

@app.route('/temp/')
def routeTemp():
    print 'get temp'
    f = open("services/temp/db.txt", "r")
    global param
    param = f.read()
    return redirect(url_for('index'))

@app.route('/light/')
def routeLight():
    print 'get light'
    f = open("services/light/db.txt", "r")
    global param
    param = f.read()
    return redirect(url_for('index'))

@app.route('/cam/')
def routeCam():
    print 'get cam'
    global param
    param = '<iframe style="width: 100%; height: 100%; border: none;" src="http://192.168.87.105:8080/?action=stream"></iframe>'
    return redirect(url_for('index'))

@app.route('/services/')
def routeServices():
    global param
    CMD = "ps -Af | grep python | cut -d ' ' -f 22 > temp.txt"
    status = os.system(CMD)
    print 'services [status='+str(status)+']'
    param = ''
    skip = ['--color=auto', 'ps', '']
    with open ('temp.txt', 'r') as fd:
        for line in fd:
            line = line.strip()
            if line in skip:
                continue
            param += '[' + line + '] '
    fd.close();
    return redirect(url_for('index'))

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('pageNotFound.html'), 404

@app.route('/index')
@app.route('/<t><l><c>')
@app.route('/')
def index(p=0):
    global param
    return render_template('index.html', p=param)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

