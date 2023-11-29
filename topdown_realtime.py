'''
This code works on realtime camera feed. The feed is captured from mobile phone using USB. Camo Studio software has to be installed in both laptop and phone.
The camo studio software on the laptop can be used to select the camera, fix the resolution, select watermarks and etc.
Press Q to Quit

Camo for PC: https://reincubate.com/camo/
Camo for Android: https://play.google.com/store/apps/details?id=com.reincubate.camo&hl=en_US&gl=US&pli=1
'''

import cv2
import numpy as np
import time

# Sharpening filter
sharp_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

#Trapezoid Overlay Parameters
isClosed = True
color = (255, 0, 0)
thickness = 6

#default trapezoid points hard coded and fixed
trapezoid_pts = np.array([[490 ,2690], [1660,2690], [2030,3350], [70,3350]], dtype='float32') # for portrait mode in 4K (3840x2160)

#rectangle points
rectangle_pts = np.array([[0,0],[1920,0],[1920,1080],[0,1080]],dtype='float32')
perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)

capture = cv2.VideoCapture(0)

# #for saving video
# frame_rate = int(capture.get(5))

# # Define the codec for the output video (e.g., XVID or H.264)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# # Create an output video file
# output_video_path = 'transformed'+'.mp4'
# out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (1920,1080))

while True:
    _, frame = capture.read()
    transformed_image = cv2.warpPerspective(frame, perspective_matrix, (1920, 1080)) 
    transformed_image = cv2.rotate(transformed_image,cv2.ROTATE_180) #rotating for front view
    transformed_image = cv2.filter2D(transformed_image, -1, sharp_kernel) #sharpening
    transformed_image = cv2.resize(transformed_image,(960,540))
    frame = cv2.polylines(frame, np.int32([trapezoid_pts]), isClosed, color, thickness)
    frame = cv2.resize(frame,(303,540)) #to match the perspective image so that output looks presentable
    subplot_image = np.concatenate((frame, transformed_image), axis=1)
    # cv2.imshow("User Feed",frame)
    # cv2.imshow("Top Down View",transformed_image)
    cv2.imshow("Feed",subplot_image)
    # out.write(subplot_image) #for saving video

    if cv2.waitKey(1) == ord("q"): #press q to exit the capture window 
        # cv2.imwrite("bone.png",subplot_image) #for debug and documentation purpose
        break

capture.release()
cv2.destroyAllWindows()

