import cv2
import numpy as np

def adaptive_median_filter(image, window_size=3):
    """Applies an adaptive median filter to an image."""
    pad_size = window_size // 2
    padded_image = np.pad(image, pad_size, mode='edge')  # Pad the image
    rows, cols = image.shape
    filtered_image = np.zeros((rows, cols), dtype=np.uint8)

    for i in range(rows):
        for j in range(cols):
            # Get the current window
            window = padded_image[i:i + window_size, j:j + window_size].flatten()
            # Calculate median
            median_value = np.median(window)

            # Set the pixel value to the median value
            filtered_image[i, j] = median_value

    return filtered_image

# Load the image
image = cv2.imread('noisy-img.png', cv2.IMREAD_GRAYSCALE)

# Apply adaptive median filter
filtered_image = adaptive_median_filter(image, window_size=3)

# Show the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Adaptive Median Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
