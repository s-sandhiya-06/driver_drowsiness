import numpy as np
from collections import deque

class DrowsinessAnalyzer:
    def __init__(self, eye_indices, threshold=0.25, window_size=5):
        self.eye_indices = eye_indices
        self.threshold = threshold
        self.ear_history = deque(maxlen=window_size)

    def calculate_ear(self, landmarks, eye):
        p1, p2, p3, p4, p5, p6 = [landmarks[i] for i in eye]

        def dist(a, b):
            return np.linalg.norm([a.x - b.x, a.y - b.y])

        vertical = dist(p2, p6) + dist(p3, p5)
        horizontal = dist(p1, p4)
        return vertical / (2.0 * horizontal)

    def analyze(self, landmarks, frame_shape):
        left_ear = self.calculate_ear(landmarks, self.eye_indices["left"])
        right_ear = self.calculate_ear(landmarks, self.eye_indices["right"])
        ear = (left_ear + right_ear) / 2.0

        self.ear_history.append(ear)
        smoothed_ear = np.mean(self.ear_history)
        return ear, smoothed_ear

    def is_drowsy(self, smoothed_ear):
        return smoothed_ear < self.threshold