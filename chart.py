import json, datetime

TIME_FORMAT = '%Y%m%d%H%M%S'
TEMP_DB_FILE = 'temp_db.txt'
LIGHT_DB_FILE = 'light_db.txt'

def timeString():
    now = datetime.datetime.now()
    return now.strftime(TIME_FORMAT)

def readTempDB():
    return string2json(TEMP_DB_FILE)

def readLightDB():
    return string2json(LIGHT_DB_FILE)

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

def lightNow():
    return readLightDB()[0]

def tempNow():
    return readTempDB()[0]

# fix some way of seeing other weeks, seeing months, years, etc.
