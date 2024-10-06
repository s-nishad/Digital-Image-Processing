import cv2
import numpy as np

# Step 1: Create a color image
width, height = 640, 480
color_image = np.zeros((height, width, 3), dtype=np.uint8)  # 3 channels (BGR)

# Set a color for a region in the image (e.g., a blue rectangle)
color_image[100:300, 200:400] = (255, 0, 0)  # Blue color

# Step 2: Display the color image
cv2.imshow('Color Image', color_image)
cv2.waitKey(0)

# Step 3: Save the color image to a file
cv2.imwrite('color_image.jpg', color_image)
