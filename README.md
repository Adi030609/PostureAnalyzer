# Real-Time Knee Tracking and Pose Estimation using OpenCV and MediaPipe

This project demonstrates real-time knee tracking and pose estimation using Python, OpenCV, and MediaPipe. It aims to track the movement of the knees dynamically and visualize the pose estimation from live video feed or pre-recorded video footage.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview
The project leverages MediaPipe's Pose estimation model to detect human body landmarks and tracks the left and right knee movements in real time. It provides both visual feedback on the video frames and a dynamic plot of knee positions to analyze the range of motion.

## Features
- **Real-Time Pose Estimation:** Uses MediaPipe's Pose estimation model to detect body landmarks.
- **Dynamic Knee Tracking:** Tracks and visualizes left and right knee positions over time.
- **Interactive Data Plotting:** Live updating plot showing knee movements with dynamic axes scaling.
- **Visual Feedback:** Displays pose landmarks on the video feed and a separate pose-only view.
- **User-Friendly Controls:** Press 'q' to exit the application.

## Requirements
To run this project, you need:
- Python 3.x
- The following Python libraries:
  - `opencv-python`
  - `mediapipe`
  - `numpy`
  - `matplotlib`

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/knee-tracking-pose-estimation.git
   cd knee-tracking-pose-estimation
   ```

2. **Install the required libraries:**
   ```bash
   pip install opencv-python mediapipe numpy matplotlib
   ```

## Usage
1. **Run the script:**
   - To use a video file for pose estimation, modify the `cap = cv2.VideoCapture()` line in the code to provide the path to your video file.
   - Alternatively, set it to `cap = cv2.VideoCapture(0)` for live camera feed.

   ```bash
   python knee_tracking_pose_estimation.py
   ```

2. **Press 'q' to exit the application.**

## Demo
Below is an example of how the system works:

1. **Pose Estimation:** The script detects human body landmarks in real time.
2. **Knee Tracking:** Plots the trajectory of knee movements.
3. **Live Visualization:** Shows the original video with pose landmarks and a separate plot of knee positions.

## Project Structure
```
knee-tracking-pose-estimation/
│
├── knee_tracking_pose_estimation.py   # Main script file
├── README.md                          # Project README file
└── requirements.txt                   # List of dependencies
```

## Customization
- **Tracking other landmarks:** You can modify the code to track different body landmarks by changing the indices used for `left_knee` and `right_knee`.
- **Changing the plot style:** Customize the plot by modifying Matplotlib settings (line color, style, etc.).
- **Adjusting the frame size:** Change the `cv2.resize()` parameters to set a different frame size.

## Contributing
Contributions are welcome! If you would like to contribute, please:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.



