import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = ~cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(gray, mask)

cv.imshow('Masked Image', masked)

""" Graylevel Histogram """
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Graylevel Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)