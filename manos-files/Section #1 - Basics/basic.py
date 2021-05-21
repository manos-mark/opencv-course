import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

""" Converting to grayscale """
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# cv.imshow('Gray', gray)

""" Blur """
blured = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blured', blured)

""" Edge Cascade """
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

""" Dilating the image """
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

""" Eroding """
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

""" Resize """
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

""" Cropping """
cropped = img[50:200, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)