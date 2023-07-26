import os

SERVICES_FILE = 'services.txt'
SERVICES_CMD = 'ps -Af | grep Python | rev | cut -d \'/\' -f 1 | rev > ' + SERVICES_FILE
UPTIME_FILE = 'uptime.txt'
UPTIME_CMD = "uptime > " + UPTIME_FILE

def services():
    status = os.system(SERVICES_CMD)
    s = ''
    skip = ['--color=auto', 'ps', '']
    with open (SERVICES_FILE, 'r') as fd:
        for line in fd:
            if line in skip or 'grep' in line:
                continue
            s += line.strip() + ', '
    fd.close();
    return s

def uptime():
    # shouldnt i do this when the file is run?
    # and only get uptime
    # (not append to file) here?
    status = os.system(UPTIME_CMD)
    s = ''
    skip = ['--color=auto', 'ps', '']
    with open (UPTIME_FILE, 'r') as fd:
        for line in fd:
            s += line.strip() + ' '
    fd.close();
    return s

# fix other OS stuff like uptime, cpu/mem util

# fix way of checking on the microservices here, and be able to start/stop them
