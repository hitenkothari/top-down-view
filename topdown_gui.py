import tkinter as tk
import cv2
from PIL import Image, ImageTk

class VideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Feed App")

        # Create a label for displaying the video feed
        self.video_label = tk.Label(root)
        self.video_label.pack(padx=10, pady=10)

        # Create a button to start a new video feed
        self.start_button = tk.Button(root, text="Start New Video Feed", command=self.start_new_feed)
        self.start_button.pack(pady=10)

        # Initialize the video capture object
        self.cap = cv2.VideoCapture(0)  # Use 0 for default camera

        # Call the update method to start displaying the video feed
        self.update()

    def update(self):
        # Read a frame from the video feed
        ret, frame = self.cap.read()

        if ret:
            # Convert the frame to RGB format
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the frame to a PhotoImage
            img = Image.fromarray(rgb_frame)
            img = ImageTk.PhotoImage(img)

            # Update the label with the new frame
            self.video_label.img = img
            self.video_label.config(image=img)

        # Call the update method after a delay (e.g., 30 milliseconds)
        self.root.after(30, self.update)

    def start_new_feed(self):
        # Create a new window for the new video feed
        new_window = tk.Toplevel(self.root)
        new_window.title("New Video Feed")

        # Create a label for displaying the new video feed
        new_video_label = tk.Label(new_window)
        new_video_label.pack(padx=10, pady=10)

        # Initialize a new video capture object
        new_cap = cv2.VideoCapture(1)  # Use 1 for a different camera

        def update_new_feed():
            # Read a frame from the new video feed
            ret, frame = new_cap.read()

            if ret:
                # Convert the frame to RGB format
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to a PhotoImage
                img = Image.fromarray(rgb_frame)
                img = ImageTk.PhotoImage(img)

                # Update the label with the new frame
                new_video_label.img = img
                new_video_label.config(image=img)

            # Call the update method after a delay (e.g., 30 milliseconds)
            new_window.after(30, update_new_feed)

        # Call the update_new_feed method to start displaying the new video feed
        update_new_feed()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoApp(root)
    root.mainloop()
