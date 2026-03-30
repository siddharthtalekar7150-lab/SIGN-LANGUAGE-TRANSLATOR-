# train.py - trains on my 8 videos
import os
import cv2
import numpy as np
from utils import HandFinder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib


class MySignTrainer:
    def __init__(self):
        self.finder = HandFinder()
        self.sign_names = []
        self.X = []
        self.y = []

    def load_(self):
        print("Loading Currently...")
        videos = ["ADDRESS.mp4", "AGE.mp4", "hello.mp4", "HOME.mp4",
                  "HOW ARE YOU.mp4", "KEEP SMILING.mp4", "NAME.mp4", "NATIVE ADDRESS.mp4"]

        for video in videos:
            path = os.path.join("data", video)
            name = video.replace(".mp4", "").title()
            self.sign_names.append(name)

            cap = cv2.VideoCapture(path)
            frames = []
            while len(frames) < 30:
                ret, frame = cap.read()
                if not ret:
                    break
                points = self.finder.get_hand(frame)
                frames.append(points)
            cap.release()

            while len(frames) < 30:
                frames.append(frames[-1])
            self.X.append(frames[:30])
            self.y.append(len(self.sign_names) - 1)
            print(f"Loaded: {name}")

    def train(self):
        X = np.array(self.X)
        y = np.array(self.y)

        model = Sequential()
        model.add(LSTM(64, return_sequences=True, input_shape=(30, 42)))
        model.add(LSTM(32))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(len(self.sign_names), activation='softmax'))

        model.compile(optimizer='adam', loss='sparse_categorical_cross entropy', metrics=['accuracy'])
        print("Training my model...")
        model.fit(X, y, epochs=30, batch_size=2)

        os.makedirs("model", exist_ok=True)
        model.save("model/prince_final.h5")
        joblib.dump(self.sign_names, "model/prince_labels.pkl")
        print("TRAINING COMPLETE!")


# Run training
trainer = MySignTrainer()
trainer.load_()
trainer.train()
