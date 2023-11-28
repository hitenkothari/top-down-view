import cv2
import numpy as np
import time

sharp_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

#overlay parameters
isClosed = True
color = (255, 0, 0)
thickness = 2


#trapezoid points, have to be pakka finalized
trapezoid_pts = np.array([[490 ,2690], [1660,2690], [2030,3350], [70,3350]], dtype='float32') # for portrait mode on 2511 4K

#size of window//can be experimented
rectangle_pts = np.array([[0,0],[1920,0],[1920,1080],[0,1080]],dtype='float32')
perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)

capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    transformed_image = cv2.warpPerspective(frame, perspective_matrix, (1920, 1080)) 
    transformed_image = cv2.rotate(transformed_image,cv2.ROTATE_180)
    transformed_image_s = cv2.filter2D(transformed_image, -1, sharp_kernel) #sharpening
    transformed_image_s = cv2.resize(transformed_image_s,(960,540))
    frame = cv2.polylines(frame, np.int32([trapezoid_pts]), isClosed, color, thickness)
    frame = cv2.resize(frame,(303,540))
    subplot_image = np.concatenate((frame, transformed_image_s), axis=1)
    # cv2.imshow("User Feed",frame)
    # cv2.imshow("Top Down View",transformed_image_s)
    cv2.imshow("Feed",subplot_image)

    if cv2.waitKey(1) == ord("x"): #press x to exit the capture window and take a photo image saved as test.png (will be replaced for each capture)
        cv2.imwrite("test.png",frame)
        break

capture.release()
cv2.destroyAllWindows()

