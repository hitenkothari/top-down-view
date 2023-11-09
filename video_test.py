import numpy as np
import cv2 as cv

cap = cv.VideoCapture('test_04_11/20231104_215456.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('frame', gray)
    cv.imshow('frame',frame)
    if cv.waitKey(33) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
