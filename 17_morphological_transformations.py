import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('smarties.png', cv.IMREAD_GRAYSCALE)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)

dilated = cv.dilate(mask, kernel, iterations=1)
eroded = cv.erode(mask, kernel, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=1)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=1)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel, iterations=1)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel, iterations=1)

titles = ['ORIGINAL', 'MASK', 'DILATED', 'ERODED', 'OPENING', 'CLOSING', 'MG', 'TH']
images = [img, mask, dilated, eroded, opening, closing, mg, th]

for i in range(len(titles)):
    plt.subplot(2, 4, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()
