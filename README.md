**Simple Image Recognition System (Facial Recognition)**
Project Overview
This project implements a basic, real-time facial recognition system using Python and OpenCV, demonstrating fundamental image processing and object detection techniques via a live webcam feed.

Features
Real-time face detection.

Uses pre-trained Haar Cascade classifiers.

Highlights detected faces with bounding boxes.

Webcam integration.

Technologies
Python 3.x

OpenCV (cv2)

NumPy

System Requirements
Computer with a webcam.

Python 3.6+ (Miniconda/Anaconda recommended).

Internet connection (for setup).

Project Structure
simple-face-recognition-opencv/
│
├── .gitignore
├── README.md
├── requirements.txt
├── LICENSE
│
└── src/
    ├── face_recognition_app.py
    └── haarcascade_frontalface_default.xml

Setup & Installation
Clone Repository:

git clone https://github.com/YOUR_USERNAME/simple-face-recognition-opencv.git
cd simple-face-recognition-opencv

Create requirements.txt & LICENSE:

requirements.txt (in root):

opencv-python~=4.9.0.80
numpy~=1.26.0

LICENSE (in root): Standard MIT License (replace [YEAR] and [YOUR NAME]).

Download Haar Cascade Classifier:

Save haarcascade_frontalface_default.xml from OpenCV GitHub into the src/ folder.

Install Libraries (using Conda - Recommended):

Open Miniconda Prompt (as Administrator).

cd C:\Users\hp\Desktop\codeclause\simple-face-recognition-opencv

conda install -c conda-forge opencv numpy (Type y to confirm).

How to Run
Open Miniconda Prompt.

Navigate to src directory:

cd C:\Users\hp\Desktop\codeclause\simple-face-recognition-opencv\src

Execute script:

python face_recognition_app.py

Press q to exit the application window.

Code Overview
face_recognition_app.py initializes the webcam, converts frames to grayscale, uses haarcascade_frontalface_default.xml to detect faces, draws blue rectangles around them, and displays the live feed.

Troubleshooting
Classifier not found: Ensure haarcascade_frontalface_default.xml is in src/ and correctly named.

Webcam not opening: Check connection, close other apps, restart computer.

Permission errors (EnvironmentNotWritableError): Run Miniconda Prompt as Administrator.

Warnings (GStreamer, QMimeDatabase): Usually non-critical if the app runs.

Contributing
Contributions are welcome! Feel free to fork, open issues, or submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.
