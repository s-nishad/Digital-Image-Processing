import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread('edge.png', cv2.IMREAD_GRAYSCALE)

# Step 2: Perform a 2D Fourier Transform
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)

# Step 3: Create a mask to filter out high-frequency components
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2  # Calculate the center of the spectrum
mask = np.zeros((rows, cols), np.uint8)
mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1  # Define a circular region as the low-pass filter

# Step 4: Apply the mask to the Fourier spectrum
filtered_spectrum = f_transform_shifted * mask

# Step 5: Perform an inverse Fourier Transform to get the filtered image
filtered_image = np.fft.ifft2(np.fft.ifftshift(filtered_spectrum)).real

# Step 6: Display the original image and the filtered image
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.axis('off')
plt.subplot(122), plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image'), plt.axis('off')
plt.show()
