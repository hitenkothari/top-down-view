'''
This code works on realtime camera feed. The feed is captured from mobile phone using USB. Camo Studio software has to be installed in both laptop and phone.
The camo studio software on the laptop can be used to select the camera, fix the resolution, select watermarks and etc.
This code allows user to zoom in and zoom out of desk.
Press Q to Quit
Press Z to Zoom In
Press X to Zoom Out
Press D for Default Zoom

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

#Trapezoid Points
tl=[490 ,2690]
tr=[1660,2690]
br=[2030,3350]
bl=[70,3350]

#Zoom Factor
delta_x = 25
delta_y = 25
i=0

#default trapezoid points 
trapezoid_pts = np.array([[490 ,2690], [1660,2690], [2030,3350], [70,3350]], dtype='float32') # for portrait mode on 2511 4K

#rectangle points
rectangle_pts = np.array([[0,0],[1920,0],[1920,1080],[0,1080]],dtype='float32')
perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)

capture = cv2.VideoCapture(0)

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

    if cv2.waitKey(1) == ord("q"): #press q to exit the capture window
        # cv2.imwrite("test.png",frame) #for debug purpose
        break
    elif cv2.waitKey(1) == ord("z") and i<5:  # Press z to zoom in
        i+=1
        trapezoid_pts = np.array([[tl[0]+i*delta_x,tl[1]+i*delta_y],[tr[0]-i*delta_x,tr[1]+i*delta_y],[br[0]-i*delta_x*2,br[1]-i*delta_y*2],[bl[0]+i*delta_x*2,bl[1]-i*delta_y*2]], dtype='float32')
        perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)
        print("Zooming in")
    elif cv2.waitKey(1) == ord("x") and i>0:  # Press x to zoom out
        i-=1
        trapezoid_pts = np.array([[tl[0]+i*delta_x,tl[1]+i*delta_y],[tr[0]-i*delta_x,tr[1]+i*delta_y],[br[0]-i*delta_x*2,br[1]-i*delta_y*2],[bl[0]+i*delta_x*2,bl[1]-i*delta_y*2]], dtype='float32')
        perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)
        print("Zooming out")
    elif cv2.waitKey(1) == ord("d"): # Press d to default zoom
        i=0
        trapezoid_pts = np.array([[tl[0]+i*delta_x,tl[1]+i*delta_y],[tr[0]-i*delta_x,tr[1]+i*delta_y],[br[0]-i*delta_x*2,br[1]-i*delta_y*2],[bl[0]+i*delta_x*2,bl[1]-i*delta_y*2]], dtype='float32')
        perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)
        print("Default")

capture.release()
cv2.destroyAllWindows()