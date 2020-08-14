import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread('image_1.png')
cv2.imshow('image1', img1)
cv2.imshow('image2', img2)

bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)

cv2.imshow('Bitwise And', bitAnd)
cv2.imshow('Bitwise Or', bitOr)
cv2.imshow('Bitwise Xor', bitXor)
cv2.imshow('Bitwise Not 1', bitNot1)


cv2.waitKey(0)
cv2.destroyAllWindows()
