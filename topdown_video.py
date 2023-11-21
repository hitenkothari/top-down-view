import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import time

# Open the input video file
input_video_path = 'test_video.mp4'
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
trapezoid_pts = np.array([[504,2767], [1526,2750], [1800,3283], [166,3318]], dtype='float32')
rectangle_pts = np.array([[0, 0], [400, 0], [400, 300], [0, 300]], dtype='float32')
perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)
# Create an output video file
output_video_path = 'output_video.mp4'

out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (400, 300))
#start_time = time.time()
frame_count = 0
#print(start_time)
ret, frame = cap.read()
while True:
    ret, frame = cap.read()

    if not ret:
        break

    #img = frame.astype("float32")/255.0
    #img = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    

# Apply the perspective transformation to the image
    transformed_image = cv2.warpPerspective(frame, perspective_matrix, (400, 300))  
    transformed_image = cv2.rotate(transformed_image,cv2.ROTATE_180)
    out.write(transformed_image)
    frame_count += 1
    #cv2_imshow(frame)
    #cv2_imshow(transformed_image)
    #cv2.imwrite('downloaded_image.jpg', frame)
'''
    print(time.time())
    if time.time() - start_time >= 5:
        fps = frame_count/(time.time() - start_time)
        print(f"FPS: {fps:.2f}")
        '''
# Release the video objects
cap.release()
out.release()
print(frame_count)
# Close all OpenCV windows
#cv2.destroyAllWindows()