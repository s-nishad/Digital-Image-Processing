import cv2
import numpy as np

# Step 1: Load an image
image = cv2.imread('edge.png')

# Step 2: Display the image
cv2.imshow('Select a Color', image)
cv2.waitKey(0)

# Step 3: Get user input for a point (color) in the image
print("Click on the image to select a color.")
print("Press any key after selecting the color.")
point = cv2.selectROI(image)
selected_color = image[int(point[1]):int(point[1] + point[3]), int(point[0]):int(point[0] + point[2])]

# Step 4: Extract the R, G, and B values of the selected color
B, G, R = np.mean(selected_color, axis=(0, 1))

print(f"R: {R}, G: {G}, B: {B}")

# Step 5: Close the image window
cv2.destroyAllWindows()
