from subprocess import call

#call ("tesseract test1.png  out1", shell=True)
#print("OCR complete")
call("raspistill -o /BrailleI/pic.jpg", shell=True)
