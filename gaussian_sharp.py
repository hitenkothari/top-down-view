'''Code to implement gaussian sharpening to warped image. The other hsarp filter seems to be working better hence this was dropped'''

import cv2
import numpy as np

def gaussian_sharpening(color_image):
    # Convert the image to float32 for better precision
    color_image = color_image.astype(np.float32) / 255.0

    # Split the color image into individual channels
    b, g, r = cv2.split(color_image)

    # Apply Gaussian blur to each channel
    blurred_b = cv2.GaussianBlur(b, (5, 5), 1)
    blurred_g = cv2.GaussianBlur(g, (5, 5), 1)
    blurred_r = cv2.GaussianBlur(r, (5, 5), 1)

    # Calculate the sharpened channels by subtracting the blurred channels from the original channels
    sharpened_b = np.clip(2.0 * b - blurred_b, 0, 1.0)
    sharpened_g = np.clip(2.0 * g - blurred_g, 0, 1.0)
    sharpened_r = np.clip(2.0 * r - blurred_r, 0, 1.0)

    # Merge the sharpened channels back into a color image
    sharpened_image = cv2.merge([sharpened_b, sharpened_g, sharpened_r])
    return sharpened_image