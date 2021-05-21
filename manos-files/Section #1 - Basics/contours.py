import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

""" Find edges using Blur & Canny """
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

""" Using Threshold """
ret, thresh = cv.threshold(gray, cv.THRESH_OTSU, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

""" Find & Draw Contours """
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contours', blank)

cv.waitKey(0)