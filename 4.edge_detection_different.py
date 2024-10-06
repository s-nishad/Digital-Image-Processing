import cv2
#import numpy as np
# Step 1: Load the image
image = cv2.imread('edge.png')

# Step 2: Apply a bilateral filter for noise reduction and edge preservation
bilateral_filtered = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

# Step 3: Perform edge detection (e.g., using the Canny edge detector)
edges = cv2.Canny(bilateral_filtered, 100, 200)  # You can adjust the threshold values

# Step 4: Display the original image, bilateral-filtered image, and edge-detected image
cv2.imshow('Original Image', image)
cv2.imshow('Bilateral Filtered Image', bilateral_filtered)
cv2.imshow('Edge Detected Image', edges)

# Step 5: Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
