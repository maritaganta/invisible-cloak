import cv2
import numpy as np
import time

import cv2

def capture_instant_image(device_index=0, output_path='captured_image.jpg'):

    # Open the webcam
    cap = cv2.VideoCapture(device_index)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print(f"Error: Cannot access camera with index {device_index}.")
        return
    
    for i in range(30):
        temp = cap.read()

    # Capture a single frame
    ret, frame = cap.read()

    # Release the webcam
    cap.release()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Failed to capture image.")
        return

    # Save the captured frame to a file
    cv2.imwrite(output_path, frame)
    print(f"Image captured and saved to {output_path}.")

    # Optionally display the captured image
    cv2.imshow('Captured Image', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage



def read_camera_stream(device_index:int=0):

    background = cv2.imread("captured_image.jpg")

    cap = cv2.VideoCapture(device_index)

    if not cap.isOpened():
        print(f"Error: Cannot access camera with index: {device_index}")

    lower_bound = np.array([15, 100, 100])
    upper_bound = np.array([30, 255, 255])


    while True:
        ret, frame = cap.read()
        
        if ret:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_bound, upper_bound)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.int8), iterations=2)
            mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.int8), iterations=2)
            mask_inv = cv2.bitwise_not(mask)
            blacked_out = cv2.bitwise_and(frame, frame, mask=mask_inv)
            coming_in = cv2.bitwise_and(background, background, mask=mask)

            result = cv2.add(blacked_out, coming_in)
            cv2.imshow("Incoming Stream", result)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            print("Failed to grab frame")

    cap.release()
    cv2.destroyAllWindows()

        


capture_instant_image()
read_camera_stream()