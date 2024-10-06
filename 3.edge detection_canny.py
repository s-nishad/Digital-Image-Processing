import cv2
import numpy as np


def gaussian_blur(image, kernel_size=5, sigma=1):
    """Apply Gaussian blur to the image."""
    k = kernel_size // 2
    kernel = np.zeros((kernel_size, kernel_size), dtype=np.float32)

    for x in range(-k, k + 1):
        for y in range(-k, k + 1):
            kernel[x + k, y + k] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))

    kernel /= np.sum(kernel)

    rows, cols = image.shape
    blurred = np.zeros((rows, cols), dtype=np.float32)

    for i in range(k, rows - k):
        for j in range(k, cols - k):
            blurred[i, j] = np.sum(kernel * image[i - k:i + k + 1, j - k:j + k + 1])

    return blurred


# Load the image
image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

# Step 1: Apply Gaussian Blur
blurred_image = gaussian_blur(image)

# Step 2: Sobel Edge Detection (as done before)
sobel_x = np.array([[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]])

sobel_y = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])

rows, cols = blurred_image.shape
gradient_magnitude = np.zeros((rows, cols), dtype=np.float32)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        gx = np.sum(sobel_x * blurred_image[i - 1:i + 2, j - 1:j + 2])
        gy = np.sum(sobel_y * blurred_image[i - 1:i + 2, j - 1:j + 2])
        gradient_magnitude[i, j] = np.sqrt(gx ** 2 + gy ** 2)

gradient_magnitude = (gradient_magnitude / gradient_magnitude.max() * 255).astype(np.uint8)

# Show the images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image.astype(np.uint8))
cv2.imshow('Canny-like Edges', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
