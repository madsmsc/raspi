from flask import Flask, render_template, redirect, url_for, jsonify

app = Flask(__name__)

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

# fix other OS stuff like uptime, cpu/mem util

# fix way of checking on the microservices here, and be able to start/stop them

@app.route('/services/')
def routeServices():
    return jsonify(readService())

if __name__ == '__main__':
    app.run(debug=True, port=5003)
