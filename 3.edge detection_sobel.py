import cv2
import numpy as np

# Load the image
image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

# Define Sobel kernels
sobel_x = np.array([[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]])

sobel_y = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])

# Get dimensions of the image
rows, cols = image.shape

# Create an empty image to store the gradient
gradient_magnitude = np.zeros((rows, cols), dtype=np.float32)

# Apply Sobel filters
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        # Convolve with Sobel kernels
        gx = np.sum(sobel_x * image[i - 1:i + 2, j - 1:j + 2])
        gy = np.sum(sobel_y * image[i - 1:i + 2, j - 1:j + 2])

        # Calculate the gradient magnitude
        gradient_magnitude[i, j] = np.sqrt(gx ** 2 + gy ** 2)

# Normalize the gradient magnitude to the range [0, 255]
gradient_magnitude = (gradient_magnitude / gradient_magnitude.max() * 255).astype(np.uint8)

# Show the original image and the gradient
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Edges', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
