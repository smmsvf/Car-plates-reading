from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pytesseract import image_to_string
import re
#convertir imatge en escala de grisos havia de ser png

img = Image.open('indice.png').convert('LA')
img.save('greyscale.png')

# edge detection jugant amb canny i matplotlib
img = cv2.imread('greyscale.png',0)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.savefig('sortida.png')


#OCR AMB PYTESSERACT

text=image_to_string('sortida.png',config='--psm 11')

# PATRO DE REGULAR EXPRESSIONS PER FILTRAR EL "SOROLL" LLEGIT
# dos numeros o lletres un espai tres lletres o numeros un espai i dos numeros o lletres
#regex = re.compile("[0-9A-Z]{2}\s[0-9A-Z]{3}\s[0-9A-Z]{2}")
#quatre numeros un espai i tres lletres
#regex = re.compile("[0-9]{4}\s[A-Z]{3}")
#filtrat dos lletres un espai i cinc numeros
regex = re.compile("[A-Z]{2}\s[0-9]{5}")
print(text)
print('FILTRAT REGEX')
print(regex.findall(text))
