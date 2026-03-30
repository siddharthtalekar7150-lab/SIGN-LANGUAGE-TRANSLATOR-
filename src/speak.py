# speak.py - Hinglish voice
from gtts import gTTS
import os


class HinglishSpeaker:
    def __init__(self):
        self.name = "Hinglish Voice"

    def speak(self, word):
        hindi_words = {
            "hello": "Namaste bhai",
            "thanks": "Shukriya yaar",
            "canteen": "Canteen jaana hai",
            "hostel": "Hostel mein hoon",
            "class": "Class mein late ho gaya"
        }

        text = hindi_words.get(word, word)
        tts = gTTS(text=text, lang='hi')
        tts.save("output.mp3")
        os.system("mpg123 output.mp3")
