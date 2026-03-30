# utils.py - simple hand detector class
import cv2
import mediapipe as mp


class HandFinder:
    def __init__(self):
        self.mp = mp.solutions.hands
        self.hands = self.mp.Hands(static_image_mode=True, max_num_hands=1)

    def get_hand(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)
        points = []
        if result.multi_hand_landmarks:
            for point in result.multi_hand_landmarks[0].landmark:
                points.append(point.x)
                points.append(point.y)
        else:
            points = [0] * 42
        return points


def get_hand_points():
    return None