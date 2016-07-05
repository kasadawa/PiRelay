# https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
# https://docs.python.org/2/library/sys.html
# http://www.tutorialspoint.com/python/python_functions.htm
import RPi.GPIO as GPIO
import time,sys

def f(x):
	return {
	'1':18,
	'2':17,
	'3':15,
	'4':14,
}[x]

pinNum = f(sys.argv[1]) 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pinNum,GPIO.OUT)
GPIO.output(pinNum,1)
print not GPIO.input(pinNum)