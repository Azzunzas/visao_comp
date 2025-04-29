import cv2
import numpy as np

imagem1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
imagem2 = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)
imagem3 = cv2.imread('img3.jpg', cv2.IMREAD_GRAYSCALE)

cantos11 = cv2.goodFeaturesToTrack(imagem1, maxCorners=100, qualityLevel=0.01, minDistance=10)
cantos11 = np.int64(cantos11)

cantos12 = cv2.goodFeaturesToTrack(imagem1, maxCorners=200, qualityLevel=0.10, minDistance=2)
cantos12 = np.int64(cantos12)

cantos13 = cv2.goodFeaturesToTrack(imagem1, maxCorners=400, qualityLevel=0.30, minDistance=1)
cantos13 = np.int64(cantos13)

cantos21 = cv2.goodFeaturesToTrack(imagem2, maxCorners=100, qualityLevel=0.01, minDistance=10)
cantos21 = np.int64(cantos21)

cantos22 = cv2.goodFeaturesToTrack(imagem2, maxCorners=200, qualityLevel=0.10, minDistance=2)
cantos22 = np.int64(cantos22)

cantos23 = cv2.goodFeaturesToTrack(imagem2, maxCorners=400, qualityLevel=0.30, minDistance=1)
cantos23 = np.int64(cantos23)

cantos31 = cv2.goodFeaturesToTrack(imagem3, maxCorners=100, qualityLevel=0.01, minDistance=10)
cantos31 = np.int64(cantos31)

cantos32 = cv2.goodFeaturesToTrack(imagem3, maxCorners=200, qualityLevel=0.10, minDistance=2)
cantos32 = np.int64(cantos32)

cantos33 = cv2.goodFeaturesToTrack(imagem3, maxCorners=400, qualityLevel=0.30, minDistance=1)
cantos33 = np.int64(cantos33)

for canto11 in cantos11:
    x, y = canto11.ravel()
    cv2.circle(imagem1, (x, y), 3, 255, -1)

cv2.imshow('Shi-Tomasi', imagem1)
cv2.imwrite('.\imagens geradas\image_1_1.jpg', imagem1)
cv2.waitKey(0)

for canto12 in cantos12:
    x, y = canto12.ravel()
    cv2.circle(imagem1, (x, y), 3, 255, -1)

cv2.imshow('Shi-Tomasi', imagem1)
cv2.imwrite('.\imagens geradas\image_1_2.jpg', imagem1)
cv2.waitKey(0)

for canto13 in cantos13:
    x, y = canto13.ravel()
    cv2.circle(imagem1, (x, y), 3, 255, -1)

cv2.imshow('Shi-Tomasi', imagem1)
cv2.imwrite('.\imagens geradas\image_1_3.jpg', imagem1)
cv2.waitKey(0)

for canto21 in cantos21:
    x, y = canto21.ravel()
    cv2.circle(imagem2, (x, y), 3, 255, -1)

cv2.imshow('Shi-Tomasi', imagem2)
cv2.imwrite('.\imagens geradas\image_2_1.jpg', imagem2)
cv2.waitKey(0)

for canto22 in cantos22:
    x, y = canto22.ravel()
    cv2.circle(imagem2, (x, y), 3, 255, -1)

cv2.imshow('Shi-Tomasi', imagem2)
cv2.imwrite('.\imagens geradas\image_2_2.jpg', imagem2)
cv2.waitKey(0)

for canto23 in cantos23:
    x, y = canto23.ravel()
    cv2.circle(imagem2, (x, y), 3, 255, -1)

cv2.imshow('Shi-Tomasi', imagem2)
cv2.imwrite('.\imagens geradas\image_2_3.jpg', imagem2)
cv2.waitKey(0)

for canto31  in cantos31:
    x, y = canto31.ravel()
    cv2.circle(imagem3, (x, y), 3, 255, -1)

cv2.imshow('Shi-Tomasi', imagem3)
cv2.imwrite('.\imagens geradas\image_3_1.jpg', imagem3)
cv2.waitKey(0)

for canto32 in cantos32:
    x, y = canto32.ravel()
    cv2.circle(imagem3, (x, y), 3, 255, -1)

cv2.imshow('Shi-Tomasi', imagem3)
cv2.imwrite('.\imagens geradas\image_3_2.jpg', imagem3)
cv2.waitKey(0)

for canto33 in cantos33:
    x, y = canto33.ravel()
    cv2.circle(imagem3, (x, y), 3, 255, -1)

cv2.imshow('Shi-Tomasi', imagem3)
cv2.imwrite('.\imagens geradas\image_3_3.jpg', imagem3)
cv2.waitKey(0)


cv2.destroyAllWindows()
