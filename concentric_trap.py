import cv2
import numpy as np
import time


isClosed = True
 
# Blue color in BGR
color = (255, 0, 0)
 
# Line thickness of 2 px
thickness = 2

delta= 20

tl=[490 ,2690]
tr=[1660,2690]
br=[2030,3350]
bl=[70,3350]

frame = cv2.imread('concentric.png')

for i in range(4):
    trapezoid_pts = np.array([[tl[0]+i*delta,tl[1]+i*delta],[tr[0]-i*delta,tr[1]+i*delta],[br[0]-i*delta,br[1]-i*delta],[bl[0]+i*delta,bl[1]-i*delta]])
    print(trapezoid_pts)
    frame = cv2.polylines(frame, np.int32([trapezoid_pts]), isClosed, color, thickness)

cv2.imshow("tr",frame)

cv2.imwrite('con.png',frame)