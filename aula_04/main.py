import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

laplacian = cv.Laplacian(img,cv.CV_64F,ksize=31)
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=31)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=31)
sobel = cv.magnitude(sobelx, sobely)

plt.subplot(3,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,2),plt.imshow(laplacian,cmap = 'Accent')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,3),plt.imshow(sobelx,cmap = 'Accent')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,4),plt.imshow(sobely,cmap = 'Accent')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,5),plt.imshow(sobel,cmap = 'inferno_r')
plt.title('Sobels'), plt.xticks([]), plt.yticks([])

plt.show()