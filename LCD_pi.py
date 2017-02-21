#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import Adafruit_CharLCD as LCD

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

for x in range(0,3):
    lcd.message('pustules Of\nlight,')
# Wait 3 seconds

    time.sleep(3.0)
    lcd.clear()
    lcd.message('On a dead nights\nbare breasts')

    time.sleep(3.0)
    lcd.clear()
    lcd.message('a gentle\nstinking breeze')

    time.sleep(3.0)
    lcd.clear()
    lcd.message('and oozing pus\nmake up this')

    time.sleep(3.0)
    lcd.clear()
    lcd.message('CITY')

    time.sleep(3.0)
    lcd.clear()
    lcd.message('a few claws\nthat scratch')        
    
    time.sleep(3.0)
    lcd.clear()
