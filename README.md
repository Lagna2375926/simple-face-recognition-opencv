# Simple Face Recognition with OpenCV

This project implements a basic, real-time facial recognition system using **Python** and **OpenCV**, demonstrating fundamental image processing and object detection techniques via a live webcam feed.

---

## Features

- Real-time face detection  
- Uses pre-trained Haar Cascade classifiers  
- Highlights detected faces with bounding boxes  
- Seamless webcam integration  

---

## Technologies Used

- Python 3.x  
- OpenCV (`cv2`)  
- NumPy  

---

## System Requirements

- A computer with a webcam  
- Python 3.6+ (Miniconda/Anaconda recommended)  
- Internet connection (for setup)  

---

## Project Structure

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


---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/simple-face-recognition-opencv.git
cd simple-face-recognition-opencv
```

### 2. Create Required Files

- requirements.txt
```
opencv-python~=4.9.0.80
numpy~=1.26.0
```
- LICENSE
Standard MIT License

### 3. Download Haar Cascade Classifier

- Save haarcascade_frontalface_default.xml from OpenCV GitHub
- Place it inside the src/ directory.

### 4. Install Dependencies (Recommended: Conda)

```bash
# Open Miniconda Prompt (Run as Administrator)
cd C:\Users\hp\Desktop\codeclause\simple-face-recognition-opencv

conda install -c conda-forge opencv numpy
```

## How to Run

```bash
# Open Miniconda Prompt

cd C:\Users\hp\Desktop\codeclause\simple-face-recognition-opencv\src

python face_recognition_app.py
```
- Press q to exit the application window.

---

## Code Overview

- face_recognition_app.py:
Initializes webcam, converts frames to grayscale, uses haarcascade_frontalface_default.xml to detect faces, draws bounding boxes, and shows live feed using OpenCV.

---

## Troubleshooting

- Classifier not found:
Ensure haarcascade_frontalface_default.xml exists inside src/ and is correctly named.

- Webcam not opening:
Check connection, close other apps using the camera, or restart the system.

- PermissionError / EnvironmentNotWritableError:
Run Miniconda Prompt as Administrator.

- Warnings (e.g., GStreamer, QMimeDatabase):
Generally non-critical if the app is functioning.

---

## License

This project is licensed under MIT License
