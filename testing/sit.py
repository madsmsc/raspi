from gpiozero import Servo
from time import sleep

gpioPin17 = 17;
gpioPin27 = 27;

maxPW = (2.0) / 1000.0;
minPW = (1.0) / 1000.0;

servo17 = Servo(gpioPin17, min_pulse_width=minPW, max_pulse_width=maxPW)
servo27 = Servo(gpioPin27, min_pulse_width=minPW, max_pulse_width=maxPW)

while servo17.value > -1.0:
    servo17.value = servo17.value - 0.1
    servo27.value = servo27.value + 0.1
