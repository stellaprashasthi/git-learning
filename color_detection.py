import cv2
import numpy as np

# Load the image
image = cv2.imread("E:\openCV\photos\Corn.jpg")

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the yellow color in HSV
lowerLimit = np.array([20,100,100])
upperLimit = np.array([30,255,255])
# Create a mask for the yellow color
mask = cv2.inRange(hsv_image, lowerLimit, upperLimit)

# Apply the mask to the original image
yellow_image = cv2.bitwise_and(image, image, mask=mask)

# Display the yellow color image
cv2.imshow('Yellow Color Image', yellow_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
