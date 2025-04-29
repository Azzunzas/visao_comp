import cv2
import numpy as np

# Carregando imagens
imagem1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
imagem2 = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)
imagem3 = cv2.imread('img3.jpg', cv2.IMREAD_GRAYSCALE)

# Criando 3 cenários diferentes para a imagem1
harris11 = cv2.cornerHarris(imagem1, blockSize=2, ksize=3, k=0.04)
harris11 = cv2.dilate(harris11, None)
harris12 = cv2.cornerHarris(imagem1, blockSize=4, ksize=7, k=0.04)
harris12 = cv2.dilate(harris12, None)
harris13 = cv2.cornerHarris(imagem1, blockSize=8, ksize=13, k=0.04)
harris13 = cv2.dilate(harris13, None)

# Criando 3 cenários diferentes para a imagem2
harris21 = cv2.cornerHarris(imagem2, blockSize=2, ksize=3, k=0.04)
harris21 = cv2.dilate(harris21, None)
harris22 = cv2.cornerHarris(imagem2, blockSize=4, ksize=7, k=0.04)
harris22 = cv2.dilate(harris22, None)
harris23 = cv2.cornerHarris(imagem2, blockSize=8, ksize=13, k=0.04)
harris23 = cv2.dilate(harris23, None)

# Criando 3 cenários diferentes para a imagem3
harris31 = cv2.cornerHarris(imagem3, blockSize=2, ksize=3, k=0.04)
harris31 = cv2.dilate(harris31, None)
harris32 = cv2.cornerHarris(imagem3, blockSize=4, ksize=7, k=0.04)
harris32 = cv2.dilate(harris32, None)
harris33 = cv2.cornerHarris(imagem3, blockSize=8, ksize=13, k=0.04)
harris33 = cv2.dilate(harris33, None)

# Mostrando todos os cenários gerados
imagem1[harris11 > 0.01 * harris11.max()] = [255]
cv2.imshow('Harris Corner', imagem1)
cv2.imwrite('.\imagens_geradas\imagem_1_1.jpg', imagem1)
cv2.waitKey(0)

imagem1[harris12 > 0.01 * harris12.max()] = [255]
cv2.imshow('Harris Corner', imagem1)
cv2.imwrite('.\imagens_geradas\imagem_1_2.jpg', imagem1)
cv2.waitKey(0)

imagem1[harris13 > 0.01 * harris13.max()] = [255]
cv2.imshow('Harris Corner', imagem1)
cv2.imwrite('.\imagens_geradas\imagem_1_3.jpg', imagem1)
cv2.waitKey(0)

imagem2[harris21 > 0.01 * harris21.max()] = [255]
cv2.imshow('Harris Corner', imagem2)
cv2.imwrite('.\imagens_geradas\imagem_2_1.jpg', imagem2)
cv2.waitKey(0)

imagem2[harris22 > 0.01 * harris22.max()] = [255]
cv2.imshow('Harris Corner', imagem2)
cv2.imwrite('.\imagens_geradas\imagem_2_2.jpg', imagem2)
cv2.waitKey(0)

imagem2[harris23 > 0.01 * harris23.max()] = [255]
cv2.imshow('Harris Corner', imagem2)
cv2.imwrite('.\imagens_geradas\imagem_2_3.jpg', imagem2)
cv2.waitKey(0)

imagem3[harris31 > 0.01 * harris31.max()] = [255]
cv2.imshow('Harris Corner', imagem3)
cv2.imwrite('.\imagens_geradas\imagem_3_1.jpg', imagem3)
cv2.waitKey(0)

imagem3[harris32 > 0.01 * harris32.max()] = [255]
cv2.imshow('Harris Corner', imagem3)
cv2.imwrite('.\imagens_geradas\imagem_3_2.jpg', imagem3)
cv2.waitKey(0)

imagem3[harris33 > 0.01 * harris33.max()] = [255]
cv2.imshow('Harris Corner', imagem3)
cv2.imwrite('.\imagens_geradas\imagem_3_3.jpg', imagem3)
cv2.waitKey(0)

cv2.destroyAllWindows()
