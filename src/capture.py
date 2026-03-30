from h5py.h5pl import size

from utils import get_hand_points

class SignCapture:
    def __init__(self):
        self.name = "Sign Capture Module"

    def record_sign(self, sign_nam):
        print(f"Recording sign: {sign_nam}")
        data = get_hand_points()
        print(f"Captured {size(data)} frames")
        return data

    def show_message(self):
        print("Capture module ready!")