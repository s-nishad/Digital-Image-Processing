
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('Test3.jpg', 0)  # Read image as grayscale

if image is not None:
    # Apply Fourier Transform
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)

    # Define the percentage of high frequencies to discard (discretization)
    percentage = 0.1  # Modify this value to change the amount of information retained

    # Determine the shape of the image
    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2

    # Discretize the Fourier Transform
    f_shift[int(center_row - percentage * rows):int(center_row + percentage * rows),
            int(center_col - percentage * cols):int(center_col + percentage * cols)] = 0

    # Inverse Fourier Transform
    f_ishift = np.fft.ifftshift(f_shift)
    image_back = np.fft.ifft2(f_ishift)
    image_back = np.abs(image_back)

    # Display the original and discretized images
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(image_back, cmap='gray')
    plt.title('Discretized Image')
    plt.axis('off')

    plt.show()
else:
    print("Error: Unable to read the image. Please check the file path.")