import glob
import datetime
from time import sleep

baseDir = '/sys/bus/w1/devices/'
deviceFolder = glob.glob(baseDir + '28*')[0]
deviceFile = deviceFolder + '/w1_slave'

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
        f = open("db.txt","a+")
        t = readTemp()
        d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        s = '{"v":"' + str(t) + '", "d":"' + d + '"}'
        f.write(s)
        f.close()
        sleep(60*30)

run()
