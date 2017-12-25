from flask import Flask, render_template, redirect, url_for
from scripts import on, off, blink, temp, light

app = Flask(__name__)

tempValue = -1;
lightValue = -1;

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
    global tempValue
    print 'get temp'
    tempValue = temp.run()
    return redirect(url_for('index'))

@app.route('/light/')
def routeLight():
    global lightValue
    print 'get light'
    lightValue = light.run()
    return redirect(url_for('index'))

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('pageNotFound.html'), 404

@app.route('/index')
@app.route('/<t><l>')
@app.route('/')
def index(t=0, l=0):
    global tempValue, lightValue
    return render_template('index.html',
                           t=tempValue,
                           l=lightValue)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

