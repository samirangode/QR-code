import numpy as np
import cv2
from pyzbar.pyzbar import decode

#img = cv2.imread('Capture.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        print(barcode.data)
        mydata = barcode.data.decode('utf-8')
        print(mydata)
    cv2.imshow('Result',img)
    cv2.waitKey(1)
#code = decode(img)
#print(code)

#print("hello world!")