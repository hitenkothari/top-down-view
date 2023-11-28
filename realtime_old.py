import cv2
import numpy as np
import time

sharp_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

#overlay parameters
isClosed = True
color = (255, 0, 0)
thickness = 2

#trapezoid points, have to be pakka finalized
# trapezoid_pts = np.array([[1320 ,1680], [2550,1680], [2880,2120], [900,2120]], dtype='float32')
# trapezoid_pts = np.array([[490 ,2480], [1740,2480], [2090,2910], [120,2910]], dtype='float32') #for test_23_11/tab_portrait #this works good for cards tab is getting chopped a bit
trapezoid_pts = np.array([[490 ,2690], [1660,2690], [2030,3350], [70,3350]], dtype='float32') # for portrait mode on 2511 4K
# trapezoid_pts = np.array([[740 ,820], [1180,820], [1380,1080], [570,1080]], dtype='float32') # for landscape mode on 2511 UHD

#size of window//can be experimented
rectangle_pts = np.array([[0,0],[1920,0],[1920,1080],[0,1080]],dtype='float32')
perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)

capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    transformed_image = cv2.warpPerspective(frame, perspective_matrix, (1920, 1080)) 
    transformed_image = cv2.rotate(transformed_image,cv2.ROTATE_180)
    # transformed_image_g = gaussian_sharpening(transformed_image)
    transformed_image_s = cv2.filter2D(transformed_image, -1, sharp_kernel) #sharpening
    # transformed_image = cv2.resize(transformed_image,(960,540))
    transformed_image_s = cv2.resize(transformed_image_s,(960,540))
    # transformed_image_g = cv2.resize(transformed_image_g,(960,540))
    frame = cv2.polylines(frame, np.int32([trapezoid_pts]), isClosed, color, thickness)
    cv2.imshow("OG",frame)
    # cv2.imshow("TDV",transformed_image)
    cv2.imshow("TDVSHarpen",transformed_image_s)
    # cv2.imshow("TDVGaussSHarpen",transformed_image_g)

    if cv2.waitKey(1) == ord("x"): #press x to exit the capture window and take a photo image saved as test.png (will be replaced for each capture)
        cv2.imwrite("test2511.png",frame)
        break

capture.release()
cv2.destroyAllWindows()

