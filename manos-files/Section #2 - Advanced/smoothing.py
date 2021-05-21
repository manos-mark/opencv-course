import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('img', img)

""" Averaging """
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

""" Gaussian """
gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gaussian)

""" Median """
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

""" Bilateral """
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)