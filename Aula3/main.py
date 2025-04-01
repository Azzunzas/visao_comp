import cv2

imagem1 = cv2.imread('curitiba.jpg')
imagem2 = cv2.imread('porto.jpg')
imagem3 = cv2.imread('saopaulo.jpg')

# Converter para escala de cinza
imagem_cinza1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
imagem_cinza2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)
imagem_cinza3 = cv2.cvtColor(imagem3, cv2.COLOR_BGR2GRAY)

# Aplicar Curitiba
_, img_bin1 = cv2.threshold(imagem_cinza1, 170, 230, cv2.THRESH_BINARY)
cv2.namedWindow("Curitiba", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Curitiba", 800, 600)

_, img_bin_inv1 = cv2.threshold(imagem_cinza1, 170, 230, cv2.THRESH_BINARY_INV)

_, img_trunc1 = cv2.threshold(imagem_cinza1, 170, 230, cv2.THRESH_TRUNC)

_, img_tozero1 = cv2.threshold(imagem_cinza1, 170, 230, cv2.THRESH_TOZERO)

_, img_tozero_inv1 = cv2.threshold(imagem_cinza1, 170, 230, cv2.THRESH_TOZERO_INV)

# Imagem segmentada binária 1
cv2.imshow("Curitiba Imagem Original", imagem1)
cv2.waitKey(0)
cv2.imshow("Curitiba THRESH_BINARY", img_bin1)
cv2.waitKey(0)
cv2.imshow("Curitiba THRESH_BINARY_INV", img_bin_inv1)
cv2.waitKey(0)
cv2.imshow("Curitiba THRESH_TRUNC", img_trunc1)
cv2.waitKey(0)
cv2.imshow("Curitiba THRESH_TOZERO", img_tozero1)
cv2.waitKey(0)
cv2.imshow("Curitiba THRESH_TOZERO_INV", img_tozero_inv1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Aplicar Porto Alegre
_, img_bin2 = cv2.threshold(imagem_cinza2, 150, 210, cv2.THRESH_BINARY)
cv2.namedWindow("Porto Alegre", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Porto Alegre", 800, 600)

_, img_bin_inv2 = cv2.threshold(imagem_cinza2, 150, 210, cv2.THRESH_BINARY_INV)

_, img_trunc2 = cv2.threshold(imagem_cinza2, 150, 210, cv2.THRESH_TRUNC)

_, img_tozero2 = cv2.threshold(imagem_cinza2, 150, 210, cv2.THRESH_TOZERO)

_, img_tozero_inv2 = cv2.threshold(imagem_cinza2, 150, 210, cv2.THRESH_TOZERO_INV)

# Imagem segmentada binária 2
cv2.imshow("Porto Alegre Imagem Original", imagem2)
cv2.waitKey(0)
cv2.imshow("Porto Alegre THRESH_BINARY", img_bin2)
cv2.waitKey(0)
cv2.imshow("Porto Alegre THRESH_BINARY_INV", img_bin_inv2)
cv2.waitKey(0)
cv2.imshow("Porto Alegre THRESH_TRUNC", img_trunc2)
cv2.waitKey(0)
cv2.imshow("Porto Alegre THRESH_TOZERO", img_tozero2)
cv2.waitKey(0)
cv2.imshow("Porto Alegre THRESH_TOZERO_INV", img_tozero_inv2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Aplicar Sao Paulo
_, img_bin3 = cv2.threshold(imagem_cinza3, 180, 240, cv2.THRESH_BINARY)
cv2.namedWindow("Sao Paulo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Sao Paulo", 800, 600)

_, img_bin_inv3 = cv2.threshold(imagem_cinza3, 180, 240, cv2.THRESH_BINARY_INV)

_, img_trunc3 = cv2.threshold(imagem_cinza3, 180, 240, cv2.THRESH_TRUNC)

_, img_tozero3 = cv2.threshold(imagem_cinza3, 180, 240, cv2.THRESH_TOZERO)

_, img_tozero_inv3 = cv2.threshold(imagem_cinza3, 180, 240, cv2.THRESH_TOZERO_INV)

# Imagem segmentada binária 3
cv2.imshow("Sao Paulo Imagem Original", imagem3)
cv2.waitKey(0)
cv2.imshow("Sao Paulo THRESH_BINARY", img_bin3)
cv2.waitKey(0)
cv2.imshow("Sao Paulo THRESH_BINARY_INV", img_bin_inv3)
cv2.waitKey(0)
cv2.imshow("Sao Paulo THRESH_TRUNC", img_trunc3)
cv2.waitKey(0)
cv2.imshow("Sao Paulo THRESH_TOZERO", img_tozero3)
cv2.waitKey(0)
cv2.imshow("Sao Paulo THRESH_TOZERO_INV", img_tozero_inv3)
cv2.waitKey(0)
cv2.destroyAllWindows()
