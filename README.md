# VIT SignAssist – Real-Time Indian Sign Language Translator  
**SIDDHARTH TALEKAR | VIT Bhopal | March 2026**

### Project Title
Real-Time Indian Sign Language Communication Assistant for Hearing-Impaired Students

### Overview of the Project
A real-time translator that recognizes 8 daily-communication Indian Sign Language gestures using a webcam and converts them into spoken English with Indian accent.  
The system helps hearing-impaired students communicate basic personal details and greetings easily in classrooms, hostels, and placement interviews.

### Features
- Live hand sign detection using MediaPipe
- Custom LSTM model trained on personally collected dataset
- Real-time prediction and speech output in Indian accent
- Clean modular code with classes and proper comments
- Three major functional modules (Capture → Process → Voice Output)

### Technologies/Tools Used
- Python 3
- OpenCV
- MediaPipe Hands
- TensorFlow / Keras
- gTTS (Text-to-Speech)
- NumPy, joblib
- Git & GitHub

### Recognized Signs
1. ADDRESS
2. AGE
3. HELLO
4. HOME
5. HOW ARE YOU
6. KEEP SMILING
7. NAME
8. NATIVE ADDRESS

### Steps to Install & Run the Project (Exactly as Required)

```bash
git clone https://github.com/brahmanprince/sign-language-translator.git
cd sign-language-translator

python -m venv venv
source venv/bin/activate          # Linux (VIT Bhopal lab)

pip install -r requirements.txt

python src/train.py               # First time only – trains the model
python src/main.py                # Live demo
