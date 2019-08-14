from flask import Flask, render_template, redirect, url_for, jsonify
import os

app = Flask(__name__)

def readServices():
    CMD = 'ps -Af | grep Python | rev | cut -d \'/\' -f 1 | rev > services/os/services.txt'
    status = os.system(CMD)
    s = ''
    skip = ['--color=auto', 'ps', '']
    with open ('services/os/services.txt', 'r') as fd:
        for line in fd:
            if line in skip or 'grep' in line:
                continue
            s += line.strip() + ', '
    fd.close();
    return s

def readUptime():
    CMD = "uptime > services/os/uptime.txt"
    status = os.system(CMD)
    s = ''
    skip = ['--color=auto', 'ps', '']
    with open ('services/os/uptime.txt', 'r') as fd:
        for line in fd:
            s += line.strip() + ' '
    fd.close();
    return s

# fix other OS stuff like uptime, cpu/mem util

# fix way of checking on the microservices here, and be able to start/stop them

@app.route('/services')
def routeServices():
    return jsonify(readServices())

@app.route('/uptime')
def routeUptime():
    return jsonify(readUptime())

if __name__ == '__main__':
    app.run(debug=True, host=('0.0.0.0'), port=5003)
