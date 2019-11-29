# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:56:44 2019

@author: Ali Ahmed Shaikh
"""
from pyzbar import pyzbar
import argparse
import imutils
from PIL import Image
import cv2

#import barcode
#EAN = barcode.get_barcode_class('ean13')
#ean = EAN(u'5901234123457')
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,help="path to input image")
#args = vars(ap.parse_args())

image = cv2.imread("image.svg.png")
image = imutils.resize(image, width=400)
cv2.imshow('image', image)
barcodes = pyzbar.decode(image)
print(barcodes)