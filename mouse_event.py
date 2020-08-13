import cv2
import numpy as np

# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')

points = []


# left click to make an arrowed line and right click to show the color in another tab
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        if click_event.dotted:
            prevXY = points.pop()
            cv2.arrowedLine(img, prevXY, (x, y), (0, 0, 255), 5, cv2.LINE_AA)
            cv2.imshow('image', img)
            click_event.dotted = False
        else:
            cv2.circle(img, (x, y), 3, (0, 0, 255), -1, cv2.LINE_AA)
            points.append((x, y))
            cv2.imshow('image', img)
            click_event.dotted = True
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1, cv2.LINE_AA)
        color = np.zeros((512, 512, 3), np.uint8)
        color[:] = [blue, green, red]
        cv2.imshow('image', img)
        cv2.imshow('color', color)


click_event.dotted = False

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
