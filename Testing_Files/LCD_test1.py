import modules.I2C_LCD_driver as driver
from time import *

lcd = driver.lcd()
str=input()
length = len(str)
a = int(len(str)/4)

for x in int(len:
    if(x>=4 & x<=8):
        slice_object = slice(0,20)
        lcd.lcd_display_string(str[slice_object], x)
        str = str[20:800]
    elif(x>=9 & x<=12):
        slice_object = slice(0,20)
        lcd.lcd_display_string(str[slice_object], x)
        str = str[20:800]
