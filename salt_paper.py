import cv2
import numpy as np


def median_filter(image, window_size=3):
    """Applies a median filter to an image."""
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
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)


# Add salt-and-pepper noise to the image (for demonstration)
def add_salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    noisy_image = np.copy(image)
    total_pixels = noisy_image.size

    # Salt noise
    num_salt = np.ceil(salt_prob * total_pixels)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in noisy_image.shape]
    noisy_image[coords[0], coords[1]] = 255  # Salt noise

    # Pepper noise
    num_pepper = np.ceil(pepper_prob * total_pixels)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in noisy_image.shape]
    noisy_image[coords[0], coords[1]] = 0  # Pepper noise

    return noisy_image


# Create a noisy image
noisy_image = add_salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02)

# Apply median filter to remove noise
filtered_image = median_filter(noisy_image, window_size=3)

# Show the original, noisy, and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Median Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
