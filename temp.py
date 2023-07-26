import glob
import datetime
from time import sleep

TIME_FORMAT = "%Y-%m-%d %H:%M"
DB_FILE = "temp_db.txt"
BASE_DIR = "/sys/bus/w1/devices/"

try:
    deviceFolder = glob.glob(BASE_DIR + '28*')[0]
    deviceFile = deviceFolder + '/w1_slave'
except:
    print("face")

def readTempRaw():
    f = open(deviceFile, 'r')
    lines = f.readlines()
    f.close()
    return lines

def readTemp():
    lines = readTempRaw()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = readTempRaw()
    equalsPos = lines[1].find('t=')
    if equalsPos != -1:
        tempString = lines[1][equalsPos+2:]
        tempC = float(tempString) / 1000.0
        return tempC

def run():
    while(True):
        f = open(DB_FILE,"a+")
        t = readTemp()
        now = datetime.datetime.now()
        d = now.strftime()
        s = '{"v":"' + str(t)
        s += '", "d":"' + d + '"}'
        f.write(s)
        f.close()
        sleep(60*30)

# if sleep arg is ms, increase to 500 or 1000
