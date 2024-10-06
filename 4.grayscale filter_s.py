import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread('Test3.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Smoothing Filters
blur = cv2.GaussianBlur(gray_image, (5, 5), 0)  # Gaussian Blur

median = cv2.medianBlur(gray_image, 5)  # Median Filter

# Sharpening Filter (Laplacian)
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# Histogram Equalization
equalized_image = cv2.equalizeHist(gray_image)

# Edge Detection (Canny)
edges = cv2.Canny(gray_image, 100, 200)

# Displaying the images using Matplotlib
plt.figure(figsize=(12, 12))

plt.subplot(2, 3, 1), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(2, 3, 2), plt.imshow(gray_image, cmap='gray'), plt.title('Grayscale Image')
plt.subplot(2, 3, 3), plt.imshow(blur, cmap='gray'), plt.title('Gaussian Blur')
plt.subplot(2, 3, 4), plt.imshow(median, cmap='gray'), plt.title('Median Filter')
plt.subplot(2, 3, 5), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian Filter')
plt.subplot(2, 3, 6), plt.imshow(equalized_image, cmap='gray'), plt.title('Histogram Equalization')
plt.show()

plt.figure(figsize=(6, 6))
plt.imshow(edges, cmap='gray'), plt.title('Edge Detection (Canny)')
plt.show()