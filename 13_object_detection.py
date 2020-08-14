import cv2 as cv
import numpy as np


def nothing(x):
    pass


cap = cv.VideoCapture(0)

cv.namedWindow('Tracking')
cv.createTrackbar('LH', 'Tracking', 0, 179, nothing)
cv.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv.createTrackbar('UH', 'Tracking', 0, 179, nothing)
cv.createTrackbar('US', 'Tracking', 0, 255, nothing)
cv.createTrackbar('UV', 'Tracking', 0, 255, nothing)

while True:
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    LH = cv.getTrackbarPos('LH', 'Tracking')
    LS = cv.getTrackbarPos('LS', 'Tracking')
    LV = cv.getTrackbarPos('LV', 'Tracking')
    UH = cv.getTrackbarPos('UH', 'Tracking')
    US = cv.getTrackbarPos('US', 'Tracking')
    UV = cv.getTrackbarPos('UV', 'Tracking')

    lower = np.array([LS, LS, LV])
    upper = np.array([UH, US, UV])

    # creating mask
    mask = cv.inRange(hsv, lower, upper)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('Frame', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Result', res)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
