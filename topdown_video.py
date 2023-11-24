import cv2
import numpy as np
# from google.colab.patches import cv2_imshow
import time

# Open the input video file
input_video_path = 'test_23_11/cards_portrait.mp4'
cap = cv2.VideoCapture(input_video_path)


kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])


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

#points test
# trapezoid_pts = np.array([[673 ,2645], [1648,2645], [1968,3177], [355,3177]], dtype='float32') #for test_22_11/book_user
# trapezoid_pts = np.array([[639 ,2679], [1716,2679], [2236,3328], [154,3328]], dtype='float32') #for test_22_11/laptop_user
# trapezoid_pts = np.array([[1320 ,1680], [2550,1680], [2880,2120], [900,2120]], dtype='float32') #for test_23_11/tab_landscape #this works good for cards tab is getting chopped a bit
trapezoid_pts = np.array([[490 ,2480], [1740,2480], [2090,2910], [120,2910]], dtype='float32') #for test_23_11/tab_portrait #this works good for cards tab is getting chopped a bit

# rectangle_pts = np.array([[0,0],[1600,0],[1600,2560],[0,2560]],dtype='float32')
# rectangle_pts = np.array([[0,0],[1080,0],[1080,1920],[0,1920]],dtype='float32')
rectangle_pts = np.array([[0,0],[1920,0],[1920,1080],[0,1080]],dtype='float32')
# rectangle_pts = np.array([[0, 0], [400, 0], [400, 300], [0, 300]], dtype='float32')
perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)
# Create an output video file
output_video_path = 'cards_port_output_nosharp.mp4'

out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (1920,1080))
#start_time = time.time()
frame_count = 0
#print(start_time)
ret, frame = cap.read()
while True:
    ret, frame = cap.read()

    if not ret:
        break



# Apply the perspective transformation to the image
    transformed_image = cv2.warpPerspective(frame, perspective_matrix, (1920, 1080))  
    transformed_image = cv2.rotate(transformed_image,cv2.ROTATE_180)
    # transformed_image = cv2.filter2D(transformed_image, -1, kernel) #sharpening
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
print("Done")

