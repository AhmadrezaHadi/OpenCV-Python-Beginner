import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


img = np.zeros((300, 512, 3), np.uint8)

cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('1: ON\n 0: OFF', 'image', 1, 1, nothing)

while True:

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    switch = cv.getTrackbarPos('1: ON\n 0: OFF', 'image')

    if switch:
        img[:] = [b, g, r]

    cv.imshow('image', img)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()
