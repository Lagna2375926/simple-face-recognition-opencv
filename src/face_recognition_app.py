import cv2 # This line brings in the OpenCV library, which does all the image magic.
import numpy as np # This line brings in NumPy, a library for working with numbers in a special way that OpenCV likes.

def run_face_recognition():
    """
    This is a special block of code (called a 'function') that will do all the work:
    - It starts your webcam.
    - It finds faces in the video.
    - It draws boxes around them.
    - It shows you the video.
    """
    print("Initializing Face Recognition System...") # This will print a message in your command window.

    # --- 1. Load the Face Detection Model ---
    # We tell OpenCV where our 'haarcascade_frontalface_default.xml' file is.
    # This file contains the "rules" for finding faces.
    # IMPORTANT: Make sure this XML file is in the *same folder* as this Python script!
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # This part checks if the face detection model loaded correctly.
    if face_cascade.empty():
        print("ERROR: Could not load face detection model.")
        print("Please make sure 'haarcascade_frontalface_default.xml' is in the 'src/' folder.")
        print("You can re-download it from: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml")
        return # If it didn't load, we stop here.

    print("Face detection model loaded successfully.")

    # --- 2. Start Your Webcam ---
    # cv2.VideoCapture(0) tries to open your computer's default webcam.
    # If you have multiple webcams, you might try 1, 2, etc., instead of 0.
    cap = cv2.VideoCapture(0)

    # Check if the webcam actually opened. If not, print an error.
    if not cap.isOpened():
        print("ERROR: Could not open webcam.")
        print("Please make sure your webcam is connected and not being used by another program.")
        return # If webcam didn't open, we stop here.

    print("Webcam initialized. Starting real-time face detection...")
    print("When the video window appears, press the 'q' key to quit.")

    # --- 3. Loop: Grab Video, Find Faces, Show Video ---
    # This 'while True' means the code inside will repeat forever,
    # until we tell it to stop (by pressing 'q').
    while True:
        # 'cap.read()' grabs one frame (picture) from your webcam.
        # 'ret' tells us if grabbing the frame was successful (True/False).
        # 'frame' is the actual picture (it's like a big grid of numbers).
        ret, frame = cap.read()

        # If we couldn't grab a frame (e.g., webcam got disconnected), stop.
        if not ret:
            print("ERROR: Failed to grab frame. Exiting...")
            break

        # --- 4. Prepare the Frame for Face Detection ---
        # Our face detection model works best with grayscale (black and white) images.
        # So, we convert the colorful 'frame' into 'gray'.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # --- 5. Find Faces in the Grayscale Image ---
        # This is the core line for detecting faces!
        # - 'gray': The image we're looking in.
        # - 'scaleFactor=1.1': How much the image is shrunk at each step to find faces of different sizes.
        # - 'minNeighbors=5': How many times a potential face must be detected nearby to be considered a real face.
        # - 'minSize=(30, 30)': We ignore faces smaller than 30x30 pixels.
        # It returns a list of 'faces', where each 'face' is a set of coordinates (x, y, width, height).
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,      # You can change this (e.g., 1.05 for more accurate but slower detection)
            minNeighbors=5,       # You can change this (e.g., 3 for more detections, 6 for fewer false ones)
            minSize=(30, 30),     # Minimum size of the face to detect
            # maxSize=(200, 200)  # You could add this to ignore very large faces
        )

        # --- 6. Draw Rectangles Around the Detected Faces ---
        # We go through each 'face' we found in the 'faces' list.
        for (x, y, w, h) in faces:
            # 'cv2.rectangle' draws a rectangle on our *original color frame*.
            # - 'frame': The image to draw on.
            # - '(x, y)': The top-left corner of the rectangle.
            # - '(x+w, y+h)': The bottom-right corner of the rectangle.
            # - '(255, 0, 0)': The color of the rectangle (Blue in BGR format: Blue=255, Green=0, Red=0).
            # - '2': The thickness of the rectangle line in pixels.
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # --- 7. Show the Video (with boxes drawn) ---
        # 'cv2.imshow' displays the 'frame' in a window.
        # 'Live Face Detection' is the title of the window.
        cv2.imshow('Live Face Detection', frame)

        # --- 8. How to Quit the Program ---
        # 'cv2.waitKey(1)' waits for 1 millisecond for you to press a key.
        # '0xFF == ord('q')' checks if the key you pressed was 'q'.
        # If 'q' is pressed, we 'break' out of the 'while True' loop, ending the program.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print(" 'q' pressed. Exiting application...")
            break

    # --- 9. Clean Up After Yourself ---
    # Once the loop ends, these lines release the webcam and close all OpenCV windows.
    cap.release() # Tells the webcam to stop.
    cv2.destroyAllWindows() # Closes all windows created by OpenCV.
    print("Application closed.")

# This line means: "If this Python script is run directly, then start the 'run_face_recognition' function."
if __name__ == "__main__":
    run_face_recognition()