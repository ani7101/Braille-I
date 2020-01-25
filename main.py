import RPi.GPIO as GPIO
import time
from subprocess import call
import picamera
import modules.I2C_LCD_driver as driver
import re

SleepTime = 1
TogglePin = 11
ButtonPin = 10
run = True
TextInput = ""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TogglePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def writeLCD(InputText):
    lcd = driver.lcd()

    empty  = " " * 20

    i = 0
    j = 0

    while i<=2 :
        while j <= len(InputText):
            lcd_line1 = InputText[j:(j+20)]
            lcd_line2 = InputText[(j+20):(j+40)]
            lcd_line3 = InputText[(j+40):(j+60)]
            lcd_line4 = InputText[(j+60):(j+80)]

            lcd.lcd_display_string(lcd_line1, 1)
            lcd.lcd_display_string(lcd_line2, 2)
            lcd.lcd_display_string(lcd_line3, 3)
            lcd.lcd_display_string(lcd_line4, 4)

            time.sleep(0.8)

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

def BlindMode():
    #The raspistill is used at a timeout of 1 second and a sharpness
    #factor of 100% to increase effectivity of the OCR
    call (r"raspistill -o /home/pi/BrailleI/pic.png -t 1 -sh 100", shell=True)
    print("Image is processed (Step 1 is done)")
    #We call the OCR, to process the image and save it as text.txt in
    #the parent folder
    call (r"tesseract /home/pi/BrailleI/pic.png text", shell=True)
    filename = r"/home/pi/BrailleI/text.txt"
    print("OCR complete (Step 2 is done)")
    f = open(filename)
    content=f.read()
    print(content)
    speak(content)
    writeLCD(content)
    print("The TTS engine spoke (Step 3 is done)")

def DumbMode(TextInput):
    TextInput1 = TextInput
    TextInput1 = TextInput1.replace(" ", "_")
    TextInput1 = TextInput1.replace(".", "_____")
    TextInput1 = TextInput1.replace("!", "_____")
    TextInput1 = TextInput1.replace("?", "_____")
    speak(TextInput1)
    writeLCD(TextInput)
    print("Completed reading")

def speak(text): #Shell commands for the TTS engine (Espeak)
    #   -ven+m5 - used to use the male voice with index 7
    #   -s180 - sets reading speed to 180 Words per minute
    #   -k20 -  is used to emphasise on CAPITAL letters
    beginning= 'espeak -ven+m3 -s180 -k20 --stdout  '
    end= '| aplay  2>/dev/null'
    #the 2>/dev/null is used to remove the warnings and the error messages
    call([beginning+text+end], shell=True)

while run:
    if GPIO.input(TogglePin) == False:
        #This is for the blind mode
        if GPIO.input(ButtonPin) == False:
            # This is the part for the execution
            BlindMode()

    else:
        #This is for the dumb mode
        TextInput = input("Enter the text to be spoken : ")
        DumbMode(TextInput)

    time.sleep(SleepTime)
