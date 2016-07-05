# https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
# https://docs.python.org/2/library/sys.html
# https://docs.python.org/2/library/json.html



#getting the main GPIO libraly
import RPi.GPIO as GPIO
#time and json
import time
import json

# setting a list of used pins 
pins = [18,17,15,14]

# setting GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# create empty list 
arr = []
# for loop from 0 to 3 
for x in range(0,4) : 
	#putting all relays in on state if GPIO is not setup
	GPIO.setup(pins[x],GPIO.OUT)
	#putting the relay state in the empty list 
	arr.append(not GPIO.input(pins[x]))

# printing the list of state's in json format
print json.dumps({0:arr[0],1:arr[1],2:arr[2],3:arr[3]})

