# Invisible Cloak Application

This application mimics the "invisible cloak" effect popularized by Harry Potter, making the user disappear on camera by blending a background image with a real-time video stream. The application detects a specified color range in the HSV color space (such as a cloak) and replaces the detected area with the background, creating the illusion of invisibility.

![Alt Text](https://github.com/maritaganta/invisible-cloak/blob/master/invisible-cloak-demo.gif) 


## Features

- **Capture Background**: Capture an initial background image to use for the invisibility effect.
- **Real-Time Video Processing**: Detect and replace the specified color in real-time video feed.
- **Customizable Color Detection**: Adjust the HSV range to detect different colors.

## Requirements

- Python 3.x
- OpenCV
- NumPy


