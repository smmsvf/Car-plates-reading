from PIL import Image

import numpy as np
import pytesseract
import gphoto2
import os
import csv
import time
import imutils
import cv2

def main():
	lista = []
	comptador = 1

	while comptador<11:
		time.sleep(1)
		os.system('gphoto2 --capture-image-and-download --filename DSCN1.JPG')

		img2 = cv2.imread('DSCN1.JPG',0)
	
		img2gray = cv2.bilateralFilter(img2, 11, 17, 17)
		gray1 = cv2.GaussianBlur(img2gray, (7, 7), 3)
		crop_img = gray1[500:1828, 800:3200]

		#Read the number plate
		text = pytesseract.image_to_string(crop_img, config='--psm 3')
		text = text[1:]
		print("Detected Number is:",text)

		cv2.imwrite('DSCN1.JPG',crop_img)
	
		#os.system('tesseract DSCN1.JPG 1 -11')
		print(text)
		lista.append(text)
		
		f = open ('1.txt','w')
		for i in lista:
			f.write(i)
		f.close()

		comptador=comptador+1

	print (lista)
	file = open('lista.csv', 'w')
	spamreader = csv.writer(file)
	spamreader.writerow(lista)
	file.close()

	
main()

