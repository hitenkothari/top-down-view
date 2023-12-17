# top-down-view
Repository for ECE 5554 Computer Vision Project

This repository is to hold the top-down view project for our Computer Vision course.

Team members: Hiten Kothari, Tejas Raju, Rashmi Ravindranath

Course: Virginia Tech ECE 5554

More detailed information on project website: https://sites.google.com/vt.edu/sharesight

Device Used:

    Phone: Samsung S20FE 5G
    Platform: Android
    Camera Lens: 12 MP, f/2.2, 13mm, 123˚ (ultrawide), 1/3.0", 1.12µm
    Video Capture Information: 4K UHD 2160x3840 Portrait Mode 30FPS

    Laptop: Apple Macbook Air M1
    Platform: MacOS Sonoma 14.1

    Tripod: Joby Gorillapod Tripod with Phone Mount

Softwares Used:

    Programming Language: Python 3.10.8

    Wired Realtime Video Capturing Software: Camo Studio
        PC: https://reincubate.com/camo/
        Android: https://play.google.com/store/apps/details?id=com.reincubate.camo&hl=en_US&gl=US&pli=1

    Wireless Realtime Video Capturing Software: IP Webcam
        Android: https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US&gl=US

Folder/File Structure: <br />
    -calibration_images/         #images for camera calibration using opencv checkerboard method <br />
    -output/                     #output images for debugging <br />
    -test_13_11/                 #test media<br /> 
    -test_23_11/                 #test media<br />
    -gaussian_sharp.py           #trying different sharpening technique<br />
    -image_test.py               #testing on single image<br />
    -ipwebcam_test.py            #testing on ipcamera feed<br />
    -lens_distortion.py          #calibration and distortion correction <br />
    -realtime_old.py             #realtime feed implementation trial<br />
    -topdown_realtime_zoom.py    #realtime feed implementation with zoom<br />
    -topdown_realtime.py         #realtime feed implementaion final<br />
    -topdown_video.py            #testing on single video<br />
