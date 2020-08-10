import cv2


img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Image', img)
# Wait time till closing the window (ms), 0 for infinite
# 0xFF is for 64-bit operating systems
k = cv2.waitKey(0) & 0xFF

if k == ord('s'):
    cv2.imwrite('lena_grayscale.jpg', img)
cv2.destroyAllWindows()


