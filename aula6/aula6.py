import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('./img.jpg')

# Definir a matriz de translação
tx, ty = 10, 10
matriz_translacao = np.float32([[1, 2, tx], [0, 1, ty]])

# Aplicar a translação
imagem_transladada = cv2.warpAffine(imagem, matriz_translacao, (imagem.shape[1], imagem.shape[0]))

# Exibir resultado
cv2.imshow('Imagem Transladada', imagem_transladada)
cv2.waitKey(0)
cv2.destroyAllWindows()
