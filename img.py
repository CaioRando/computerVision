import cv2

image = cv2.imread('zuky.jpeg')
print("Largura em pixels: ", end='')
print(image.shape[1])
print("Altura em pixels: ", end='')
print(image.shape[0])
print("Quantidade de canais: ", end='')
print(image.shape[2])

cv2.imshow("MIAU", image)
cv2.waitKey(0)
cv2.imwrite("zuky.jpeg", image)