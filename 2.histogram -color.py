import cv2
import matplotlib.pyplot as plt

# Step 1: Load the grayscale and color images
grayscale_image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
color_image = cv2.imread('image.jpg')

# Step 2: Initialize histograms
histogram_grayscale = [0] * 256  # For grayscale image
histogram_red = [0] * 256  # For red channel
histogram_green = [0] * 256  # For green channel
histogram_blue = [0] * 256  # For blue channel

# Step 3: Calculate histogram for grayscale image
for i in range(grayscale_image.shape[0]):  # Iterate over rows
    for j in range(grayscale_image.shape[1]):  # Iterate over columns
        pixel_value = grayscale_image[i, j]
        histogram_grayscale[pixel_value] += 1  # Increment the count for the pixel value

# Step 4: Calculate histogram for each channel of the color image
for i in range(color_image.shape[0]):  # Iterate over rows
    for j in range(color_image.shape[1]):  # Iterate over columns
        # Extract the pixel values for each channel
        blue = color_image[i, j, 0]
        green = color_image[i, j, 1]
        red = color_image[i, j, 2]

        # Increment the count for each channel
        histogram_blue[blue] += 1
        histogram_green[green] += 1
        histogram_red[red] += 1

# Step 5: Display the histograms
plt.figure(figsize=(12, 6))

# Grayscale Histogram
plt.subplot(1, 3, 1)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(histogram_grayscale, color='gray')

# Red Channel Histogram
plt.subplot(1, 3, 2)
plt.title('Red Channel Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(histogram_red, color='red')

# Green Channel Histogram
plt.subplot(1, 3, 3)
plt.title('Green Channel Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(histogram_green, color='green')

# Blue Channel Histogram (optional)
# Uncomment if you want to include the blue channel histogram
# plt.subplot(1, 4, 4)
# plt.title('Blue Channel Histogram')
# plt.xlabel('Pixel Value')
# plt.ylabel('Frequency')
# plt.plot(histogram_blue, color='blue')

plt.tight_layout()
plt.show()
