import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv.flip(frame, 1)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower = np.array([0, 0, 0])
    upper = np.array([179, 20, 20])

    mask = cv.inRange(hsv, lower, upper)

    frame = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('image', frame)
    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
