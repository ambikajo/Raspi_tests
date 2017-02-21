#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import textwrap, sys
import Adafruit_CharLCD as LCD
from time import sleep
import os 
import RPi.GPIO as GPIO

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)



unwrapped_text = sys.stdin.read() 

print(unwrapped_text)
message = len(unwrapped_text)
lcd.message(unwrapped_text)
time.sleep(.8)
if message > 16:
     
        lcd.move_left()
   
            
lcd.clear()
