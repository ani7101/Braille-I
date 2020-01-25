from PIL import Image
import pytesseract

im = Image.open("pic.jpg") # Upload a photo in the same directory 
                           #  with the foll name and extension

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
