import cv2 as cv
import numpy as np

# note that simple thresholding only works on grayscale images
img = cv.imread('gradient.png')

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO)
_, th3 = cv.threshold(img, 70, 255, cv.THRESH_TRUNC)

cv.imshow('Image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)



cv.waitKey(0)
cv.destroyAllWindows()
