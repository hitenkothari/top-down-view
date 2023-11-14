import urllib.request
import cv2
import numpy as np
import time

URL = "http://172.30.37.33:8080"
while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    cv2.imshow('IPWebcam',img)
    
    if cv2.waitKey(1):
        break

# capture = cv2.VideoCapture(URL)
# while True:
#     _, frame = capture.read()
#     cv2.imshow('sharesight',frame)
#     if cv2.waitKey(1) == ord("x"): #press x to exit the capture window and take a photo image saved as test.png (will be replaced for each capture)
#         result,frame = capture.read()
#         cv2.imwrite("test.png",frame)
#         break
# capture.release()
# cv2.destroyAllWindows()
