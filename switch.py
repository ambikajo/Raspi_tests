 #!/usr/bin/env python
from time import sleep
import os 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

while True:
	if ( GPIO.input(21) == False ):
		print("Printing")
		os.system("/usr/games/fortune -s | python LCD_fortunes.py")
		print("Printed")


sleep(1)
	

