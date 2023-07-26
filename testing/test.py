from gpiozero import Servo
from time import sleep

gpioPin17 = 17;
gpioPin27 = 27;
correction = 0;
maxPW = (2.0 + correction) / 1000.0;
minPW = (1.0 - correction) / 1000.0;
servo17 = Servo(gpioPin17, min_pulse_width=minPW, max_pulse_width=maxPW)
servo27 = Servo(gpioPin27, min_pulse_width=minPW, max_pulse_width=maxPW)

while True:
    for v in range(0, 21):
        v2 = (float(v) - 10.0) / 10.0
        servo17.value = v2
        servo27.value = v2
        print(v2)
        sleep(0.2)

    for v in range(20, -1, -1):
        v2 = (float(v) - 10.0) / 10.0
        servo17.value = v2
        servo27.value = v2
        print(v2)
        sleep(0.2)
