import cv2
import numpy as np

imagem = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

# Criar o objeto SIFT
sift = cv2.SIFT_create()

# Detectar e computar características
keypoints, descriptors = sift.detectAndCompute(imagem, None)

# Desenhar keypoints na imagem
imagem_sift = cv2.drawKeypoints(imagem, keypoints, None)

# Exibir resultados
cv2.imshow('SIFT', imagem_sift)
cv2.imwrite('.\imagens geradas\imagem_gerada.jpg', imagem_sift)
cv2.waitKey(0)
cv2.destroyAllWindows()
