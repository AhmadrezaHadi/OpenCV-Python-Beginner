import cv2
from removing_background_trasparency_from_png_images import png_background_fix

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png', cv2.IMREAD_UNCHANGED)
img2 = png_background_fix(img2)

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))


# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .1, img2, .9, 0)

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
