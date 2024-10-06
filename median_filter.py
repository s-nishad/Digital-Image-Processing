import cv2
import numpy as np


def median_filter(image, kernel_size=3):
    """Applies a median filter to an image."""
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='edge')  # Pad the image
    rows, cols = image.shape
    filtered_image = np.zeros((rows, cols), dtype=np.uint8)

    for i in range(rows):
        for j in range(cols):
            # Extract the neighborhood
            neighborhood = padded_image[i:i + kernel_size, j:j + kernel_size]
            # Calculate the median
            filtered_image[i, j] = np.median(neighborhood)

    return filtered_image


# Load the image
image = cv2.imread('noisy-img.png', cv2.IMREAD_GRAYSCALE)

# Apply median filter
filtered_image = median_filter(image, kernel_size=3)

# Show the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Median Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
