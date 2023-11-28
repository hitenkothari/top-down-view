'''This is code is to test IP Webcam working. Download IP camera app, make sure both systems are on the same network.
Select camera specifications and module as per requirement on IP camera app and start the server.'''

import urllib.request
import cv2
import numpy as np
import time

#enter the url from the IP camera app https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US&gl=US
url = "http://10.0.1.110:8080/video"
# While loop to continuously fetching data from the Url
capture = cv2.VideoCapture(url)
while True:
    _, frame = capture.read()
    cv2.imshow('sharesight',frame)
    if cv2.waitKey(1) == ord("q"): #press x to exit the capture window and take a photo image saved as test.png (will be replaced for each capture)
        break
capture.release()
cv2.destroyAllWindows()