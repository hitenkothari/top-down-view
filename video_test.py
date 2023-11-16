# import numpy as np
# import cv2 as cv

# cap = cv.VideoCapture('test_04_11/20231104_215456.mp4')
# while cap.isOpened():
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # cv.imshow('frame', gray)
#     cv.imshow('frame',frame)
#     if cv.waitKey(33) == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()


# import cv2

# # Set the video capture device (0 for default camera)
# cap = cv2.VideoCapture("test_04_11/20231104_215456.mp4")

# # Define the codec and create a VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can change the codec as needed
# fps = 30  # Frames per second
# out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (640, 480))  # Adjust resolution as needed

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Display the frame
#     cv2.imshow('Frame', frame)

#     # Write the frame to the output video file
#     out.write(frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release everything when done
# cap.release()
# out.release()
# cv2.destroyAllWindows()

# import cv2

# # Open the video file

# video_path = 'test_13_11/cards_user.mp4'  # Replace with the path to your video file
# cap = cv2.VideoCapture(video_path)

# # Check if the video opened successfully
# if not cap.isOpened():
#     print("Error: Could not open video.")
#     exit()

# # Get information about the video
# fps = int(cap.get(cv2.CAP_PROP_FPS))
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# print(f"Video FPS: {fps}")
# print(f"Video Resolution: {width}x{height}")

# # Set the desired frame rate for playback (60 fps in this example)
# desired_fps = 30
# cap.set(cv2.CAP_PROP_FPS, desired_fps)

# # Calculate the delay for 60 fps
# delay = int(1000 / desired_fps)  # Delay in milliseconds

# # Read and display frames until the video ends
# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break  # Break the loop if the video ends

#     # Display the frame
#     cv2.imshow('Video', frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(delay) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close the window
# cap.release()
# cv2.destroyAllWindows()

import cv2
from imutils.video import VideoStream
import imutils

# Open the video file or use 0 for the default camera
video_path = 'test_13_11/earbuds_user.mp4'  # Replace with the path to your video file
vs = VideoStream(src=video_path).start()

# Allow the camera or video file to warm up
cv2.waitKey(1000)

while True:
    # Read the frame from the video stream
    frame = vs.read()

    # If the frame is None, the video stream has ended
    if frame is None:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the video stream and close the window
vs.stop()
cv2.destroyAllWindows()
