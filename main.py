# main.py
from utils import capture_background, read_camera_stream

def main():
    # Capture the background image (initial frame)
    capture_background(output_path='captured_image.jpg')

    # Start the camera stream and apply the invisible cloak effect
    read_camera_stream(background_path='captured_image.jpg')

if __name__ == "__main__":
    main()
