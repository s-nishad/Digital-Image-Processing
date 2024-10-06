import cv2
import pywt
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread('edge.png', cv2.IMREAD_GRAYSCALE)

# Step 2: Define the wavelet and level of decomposition
wavelet = 'haar'  # You can choose a different wavelet
level = 2  # You can adjust the level of decomposition

# Step 3: Perform the discrete wavelet transform (DWT)
coeffs = pywt.wavedec2(image, wavelet, level=level)

# Step 4: Display the original image and the DWT coefficients
plt.figure(figsize=(12, 6))
plt.subplot(level + 2, 1, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

for i, coeff in enumerate(coeffs):
    plt.subplot(level + 2, 1, i + 2)
    if i == 0:
        title = 'Approximation (LL)'
    else:
        title = f'Detail (L{i})'
    plt.imshow(np.uint8(coeff), cmap='gray')
    plt.title(title)

plt.tight_layout()
plt.show()
