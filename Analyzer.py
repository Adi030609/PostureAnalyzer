import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# Initialize Mediapipe Pose and drawing utilities
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Initialize video capture (video file or camera)
cap = cv2.VideoCapture(r"C:\Users\adity\OneDrive\Desktop\Learning\PostureAnalysis\Sample2.mp4")
# cap = cv2.VideoCapture(0)

# Deques to store knee points for plotting
left_knee_x = deque(maxlen=100)
left_knee_y = deque(maxlen=100)
right_knee_x = deque(maxlen=100)
right_knee_y = deque(maxlen=100)

# Set up the plot
plt.ion()
fig, ax = plt.subplots()
left_knee_plot, = ax.plot([], [], 'r-', label='Left Knee')
right_knee_plot, = ax.plot([], [], 'b-', label='Right Knee')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()

while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (600, 600))

    results = pose.process(img)

    # Draw landmarks on the image
    if results.pose_landmarks:
        mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                               mp_draw.DrawingSpec((255, 0, 0), 2, 2),
                               mp_draw.DrawingSpec((255, 0, 255), 2, 2))

        # Extract knee points
        left_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
        right_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]

        # Append knee points to the deques
        left_knee_x.append(left_knee.x)
        left_knee_y.append(left_knee.y)
        right_knee_x.append(right_knee.x)
        right_knee_y.append(right_knee.y)

        # Update the plot
        left_knee_plot.set_data(left_knee_x, left_knee_y)
        right_knee_plot.set_data(right_knee_x, right_knee_y)
        ax.set_xlim(min(left_knee_x) - 0.1, max(left_knee_x) + 0.1)
        ax.set_ylim(min(left_knee_y) - 0.1, max(left_knee_y) + 0.1)
        fig.canvas.draw()
        fig.canvas.flush_events()

    cv2.imshow("Pose Estimation", img)

    h, w, c = img.shape

    opImg = np.zeros([h, w, 3])
    opImg.fill(255)
    if results.pose_landmarks:
        mp_draw.draw_landmarks(opImg, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                               mp_draw.DrawingSpec((255, 0, 0), 2, 2),
                               mp_draw.DrawingSpec((255, 0, 255), 2, 2))
    cv2.imshow("Extraction Pose", opImg)

    if cv2.waitKey(5) & 0xFF == ord('q'):  # Press 'q' to exit the loop
        break

cap.release()
cv2.destroyAllWindows()
plt.ioff()
plt.show()