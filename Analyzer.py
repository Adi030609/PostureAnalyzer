import cv2
import mediapipe as mp
import numpy as np
from collections import deque

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

def analyze(path):
    pose = mp_pose.Pose()

    cap = cv2.VideoCapture(path)

    left_knee_x = deque(maxlen=100)
    left_knee_y = deque(maxlen=100)
    right_knee_x = deque(maxlen=100)
    right_knee_y = deque(maxlen=100)

    while True:
        ret, img = cap.read()
        if not ret:
            break

        img = cv2.resize(img, (600, 600))
        results = pose.process(img)

        annotated = img.copy()

        if results.pose_landmarks:
            mp_draw.draw_landmarks(annotated, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            left_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
            right_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]

            left_knee_x.append(left_knee.x)
            left_knee_y.append(left_knee.y)
            right_knee_x.append(right_knee.x)
            right_knee_y.append(right_knee.y)

        yield annotated, list(left_knee_x), list(left_knee_y), list(right_knee_x), list(right_knee_y)

    cap.release()
