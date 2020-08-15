import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', cv.IMREAD_UNCHANGED)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25

dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
# good for removing high frequency noise from the image
gBlur = cv.GaussianBlur(img, (5, 5), 0)
# good for salt and pepper noises
median = cv.medianBlur(img, 5)
# good for keeping the edges sharp
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)


titles = ['Original', '2D filter', 'blur', 'Gaussian Blur', 'Median', 'Bilateral Filter']
images = [img, dst, blur, gBlur, median, bilateralFilter]

for i in range(len(titles)):
    plt.subplot(2, 3, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()
#
#
# import cv2
# import numpy
#
# # read image
# src = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED)
#
# # apply guassian blur on src image
# dst = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
#
# # display input and output image
# cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))
# cv2.waitKey(0)  # waits until a key is pressed
# cv2.destroyAllWindows()  # destroys the window showing image
