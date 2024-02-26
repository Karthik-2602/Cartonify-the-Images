from google.colab import files

# Upload the image file
uploaded = files.upload()

# Get the file path
image_path = list(uploaded.keys())[0]

# code to extract edges using CV library
import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

def cartoonify_image(image_path):
    # Read the input image
    img = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if img is None:
        print("Error: Could not read the image.")
        return

    print("Image loaded successfully.")

    # Resize the image to a standard size
    print("Original Image Shape:", img.shape)
    img = cv2.resize(img, (128, 128))

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filter to reduce noise and keep edges sharp
    gray = cv2.bilateralFilter(gray, 9, 300, 300)

    # Apply edge detection using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Convert the color image to a cartoon-like image
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Combine the color image with the edges using bitwise_and
    cartoon_image = cv2.bitwise_and(color, color, mask=edges)

    # Display the original and cartoonified images using cv2_imshow()
    cv2_imshow(img)
    cv2_imshow(cartoon_image)

# Upload the image file
uploaded = files.upload()

# Get the file path
image_path = list(uploaded.keys())[0]

# Process the cartoonify function
cartoonify_image(image_path)
