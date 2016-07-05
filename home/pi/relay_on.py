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

# sys.argv[1] is the next input after the name 
# Example : 
# sudo python relay_on.py 1
# if we want to get 1 we need sys.argv[1]

pinNum = f(sys.argv[1]) 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pinNum,GPIO.OUT)
#turing on the current relay
GPIO.output(pinNum,0)
#returning the current state of the relay
print not GPIO.input(pinNum)

