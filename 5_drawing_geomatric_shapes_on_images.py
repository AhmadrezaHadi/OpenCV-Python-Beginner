import cv2
import numpy as np

# img = cv2.imread('lena.jpg', 1)
img = np.zeros((512, 512, 3), np.uint8)

img = cv2.line(img, (0, 0), (256, 256), (255, 0, 0), 5)
img = cv2.arrowedLine(img, (0, 256), (256, 256), (0, 255, 0), 5)
img = cv2.rectangle(img, (300, 0), (512, 200), (255, 255, 0), 5)
img = cv2.circle(img, (400, 400), 60, (255, 0, 255), -1)
# putText (src, text, starting_point, font, scale, BGR, thickness, Line_Type)
img = cv2.putText(img, 'OpenCV', (10, 470), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()