import cv2

imagem1 = cv2.imread('curitiba.jpg')
imagem2 = cv2.imread('porto.jpg')
imagem3 = cv2.imread('saopaulo.jpg')

# Converter para escala de cinza
imagem_cinza1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
imagem_cinza2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)
imagem_cinza3 = cv2.cvtColor(imagem3, cv2.COLOR_BGR2GRAY)

# Aplicar thresholding binário 1
_, img_bin1 = cv2.threshold(imagem_cinza1, 170, 255, cv2.THRESH_BINARY)
cv2.namedWindow("Thresholding Binário 1", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Thresholding Binário 1", 800, 600)

_, img_bin_inv1 = cv2.threshold(imagem_cinza1, 170, 255, cv2.THRESH_BINARY_INV)

_, img_trunc1 = cv2.threshold(imagem_cinza1, 170, 255, cv2.THRESH_TRUNC)

_, img_tozero1 = cv2.threshold(imagem_cinza1, 170, 255, cv2.THRESH_TOZERO)

_, img_tozero_inv1 = cv2.threshold(imagem_cinza1, 170, 255, cv2.THRESH_TOZERO_INV)

# Imagem segmentada binária 1
cv2.imshow("Thresholding Binário 1", img_bin1)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 1", img_bin_inv1)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 1", img_trunc1)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 1", img_tozero1)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 1", img_tozero_inv1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Aplicar thresholding binário 2
_, img_bin2 = cv2.threshold(imagem_cinza2, 170, 255, cv2.THRESH_BINARY)
cv2.namedWindow("Thresholding Binário 2", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Thresholding Binário 2", 800, 600)

_, img_bin_inv2 = cv2.threshold(imagem_cinza2, 170, 255, cv2.THRESH_BINARY_INV)

_, img_trunc2 = cv2.threshold(imagem_cinza2, 170, 255, cv2.THRESH_TRUNC)

_, img_tozero2 = cv2.threshold(imagem_cinza2, 170, 255, cv2.THRESH_TOZERO)

_, img_tozero_inv2 = cv2.threshold(imagem_cinza2, 170, 255, cv2.THRESH_TOZERO_INV)

# Imagem segmentada binária 2
cv2.imshow("Thresholding Binário 2", img_bin2)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 2", img_bin_inv2)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 2", img_trunc2)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 2", img_tozero2)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 2", img_tozero_inv2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Aplicar thresholding binário 3
_, img_bin3 = cv2.threshold(imagem_cinza3, 170, 255, cv2.THRESH_BINARY)
cv2.namedWindow("Thresholding Binário 3", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Thresholding Binário 3", 800, 600)

_, img_bin_inv3 = cv2.threshold(imagem_cinza3, 170, 255, cv2.THRESH_BINARY_INV)

_, img_trunc3 = cv2.threshold(imagem_cinza3, 170, 255, cv2.THRESH_TRUNC)

_, img_tozero3 = cv2.threshold(imagem_cinza3, 170, 255, cv2.THRESH_TOZERO)

_, img_tozero_inv3 = cv2.threshold(imagem_cinza3, 170, 255, cv2.THRESH_TOZERO_INV)

# Imagem segmentada binária 3
cv2.imshow("Thresholding Binário 3", img_bin3)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 3", img_bin_inv3)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 3", img_trunc3)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 3", img_tozero3)
cv2.waitKey(0)
cv2.imshow("Thresholding Binário 3", img_tozero_inv3)
cv2.waitKey(0)
cv2.destroyAllWindows()
