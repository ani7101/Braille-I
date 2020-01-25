import modules.I2C_LCD_driver as driver
import time

lcd = driver.lcd()

empty  = " " * 20
InputString = input("Enter a string")
#InputString = empty + InputString

i = 0
j = 0

while i<=2 :
    while j <= len(InputString):
        lcd_line1 = InputString[j:(j+20)]
        lcd_line2 = InputString[(j+20):(j+40)]
        lcd_line3 = InputString[(j+40):(j+60)]
        lcd_line4 = InputString[(j+60):(j+80)]

        lcd.lcd_display_string(lcd_line1, 1)
        lcd.lcd_display_string(lcd_line2, 2)
        lcd.lcd_display_string(lcd_line3, 3)
        lcd.lcd_display_string(lcd_line4, 4)

        time.sleep(1)

        lcd.lcd_display_string(empty, 1)
        lcd.lcd_display_string(empty, 2)
        lcd.lcd_display_string(empty, 3)
        lcd.lcd_display_string(empty, 4)

        j = j + 5

    i = i + 1

lcd.lcd_display_string(empty, 1)
lcd.lcd_display_string(empty, 2)
lcd.lcd_display_string(empty, 3)
lcd.lcd_display_string(empty, 4)
