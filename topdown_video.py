'''This code is to test perspective transformation on a saved video file. User has to provide path to input .mp4 file. The output transformed video will be saved in the same folder. 
The trapezoid points can be varied manually as per requirement of region of interest.
'''

import cv2
import numpy as np
import time

# Sharpening filter
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

#trapezoid points hard coded and fixed
# trapezoid_pts = np.array([[1320 ,1680], [2550,1680], [2880,2120], [900,2120]], dtype='float32') #for test_23_11/tab_landscape 4k
trapezoid_pts = np.array([[490 ,2480], [1740,2480], [2090,2910], [120,2910]], dtype='float32') #for test_23_11/tab_portrait 4k

#rectangle points
rectangle_pts = np.array([[0,0],[1920,0],[1920,1080],[0,1080]],dtype='float32')
perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)

# Open the input video file
input_video_name = 'test_23_11/tab_portrait'
input_video_path = input_video_name+'.mp4'
cap = cv2.VideoCapture(input_video_path)

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate = int(cap.get(5))

# Define the codec for the output video (e.g., XVID or H.264)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Create an output video file
output_video_path = input_video_name+'_transformed'+'.mp4'
out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (1920,1080))
frame_count = 0

ret, frame = cap.read()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    transformed_image = cv2.warpPerspective(frame, perspective_matrix, (1920, 1080))  
    transformed_image = cv2.rotate(transformed_image,cv2.ROTATE_180)
    transformed_image = cv2.filter2D(transformed_image, -1, kernel)
    out.write(transformed_image)
    frame_count += 1
    
# Release the video objects
cap.release()
out.release()
print("Transformation Completed")
# print(frame_count)
cv2.destroyAllWindows()


