import numpy as np
import cv2
import matplotlib.pyplot as plt

image=cv2.imread("test_22_11/book_user1.jpg")
uw_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(uw_image)
plt.axis("off")
plt.show()

uw_points = np.array([[735,2768],[45,3656],[2487,3656],[2044,2768]],dtype='float32')
td_points = np.array([[0,0],[1600,0],[1600,2560],[0,2560]],dtype='float32') #tablet resolution, can be changed as per requirement

h_matrix = cv2.getPerspectiveTransform(uw_points, td_points)

# Apply the perspective transformation to the image
td_image = cv2.warpPerspective(uw_image, h_matrix, (1600, 2560)) 
td_image = cv2.rotate(td_image,cv2.ROTATE_90_COUNTERCLOCKWISE)
plt.imshow(td_image)
plt.axis("off")
plt.show()
