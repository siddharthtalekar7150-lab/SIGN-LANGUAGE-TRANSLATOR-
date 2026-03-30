# main.py - live translator
import cv2
import numpy as np
import tensorflow as tf
import joblib
from utils import HandFinder
from gtts import gTTS
import os


class Translator:
    def __init__(self):
        self.finder = HandFinder()
        self.model = tf.keras.models.load_model("model/prince_final.h5")
        self.labels = joblib.load("model/prince_labels.pkl")
        self.sequence = []

    def predict_sign(self):
        if len(self.sequence) == 30:
            pred = self.model.predict(np.array([self.sequence]), verbose=0)
            return self.labels[np.argmax(pred)]
        return ""


t = Translator()
cap = cv2.VideoCapture(0)
print("Prince's Sign Language Project - Show your signs!")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    points = t.finder.get_hand(frame)
    t.sequence.append(points)
    if len(t.sequence) > 30:
        t.sequence = t.sequence[-30:]

    word = t.predict_sign()
    if word:
        cv2.putText(frame, word, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
        tts = gTTS(word, lang='en', tld='co.in')
        tts.save("temp.mp3")
        os.system("mpg123 temp.mp3 > /dev/null 2>&1")

    cv2.imshow("Prince - VIT Sign Language Project", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
