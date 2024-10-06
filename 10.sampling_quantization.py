import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('Test3.jpg')

# Display the original image
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.show()

# Image Sampling
def image_sampling(img, factor):
    sampled_img = img[::factor, ::factor]
    return sampled_img

# Image Quantization
def image_quantization(img, levels):
    quantized_img = np.floor_divide(img, 256 // levels) * (256 // levels)
    return quantized_img

# Sampling the image by a factor of 2
sampled_image = image_sampling(image, 2)

# Quantizing the image to 4 levels
quantized_image = image_quantization(image, 4)

# Display the sampled image
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(sampled_image, cv2.COLOR_BGR2RGB))
plt.title('Sampled Image (Factor: 2)')
plt.axis('off')
plt.show()

# Display the quantized image
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(quantized_image, cv2.COLOR_BGR2RGB))
plt.title('Quantized Image (Levels: 4)')
plt.axis('off')
plt.show()

#from google.colab import files
#from IPython.display import Image


# Upload file
#noisy_image =files.upload()
noisy_image = cv2.imread('Test3.jpg', 0)  # Load as grayscale