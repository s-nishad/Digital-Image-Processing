import cv2

image = cv2.imread('img.png')

r, c = image.shape[0:2]

for i in range(r):
    for j in range(c):
        image[i, j] = sum(image[i, j]) * 0.33

cv2.imshow('Grayscale Image', image)
cv2.waitKey(0)
