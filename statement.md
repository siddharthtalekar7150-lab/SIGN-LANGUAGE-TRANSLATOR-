# VIT SignAssist – Real-Time Indian Sign Language Communication Assistant  
**statement.md** | SIDDHARTH TALEKAR| VIT Bhopal | March 2026

### Problem Statement  
Hearing-impaired and deaf students at VIT often face difficulty in everyday communication when they need to share basic personal information such as their **name, age, address, native address, home location**, or simply greet someone with **hello, how are you, keep smiling**.  
In classrooms, hostels, and during placements, they rely on writing or lip-reading, which is slow, tiring, and sometimes inaccurate.

### Scope of the Project  
To build a **real-time Indian Sign Language (ISL) translator** that:
- Uses a normal laptop webcam
- Recognizes 8 essential communication signs
- Instantly displays the meaning on screen
- Speaks the word/phrase aloud in natural Indian-accent English  
→ Enabling seamless two-way communication between hearing-impaired and hearing students/faculty.

### Target Users  
- Hearing-impaired / deaf students at VIT Vellore  
- Classmates, friends, and roommates who want to communicate effortlessly  
- Faculty and placement coordinators during interviews and interactions

### High-level Features  

| Feature                         | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| Live Sign Capture               | Captures hand gestures using webcam in real time                            |
| Custom Dataset                  | 8 original videos recorded by me (ADDRESS, AGE, hello, HOME, HOW ARE YOU, KEEP SMILING, NAME, NATIVE ADDRESS) |
| Deep Learning Model             | LSTM-based sequence classification trained on my personal dataset          |
| Real-time Prediction            | Predicts and displays the sign meaning instantly                           |
| Text-to-Speech (Indian Accent)  | Speaks the recognized word/phrase using Google TTS with Indian voice       |
| Simple & Clean Interface        | Minimal UI – just webcam feed with recognized text overlay                 |

### Functional Requirements (Three Major Modules)  
1. **Sign Capture Module** – Detects and extracts hand landmarks frame-by-frame  
2. **Training & Prediction Module** – Trains LSTM model on my 8 videos and predicts live signs  
3. **Voice Output Module** – Converts recognized text to natural Indian-accent speech  

### Non-Functional Requirements (More than 4 satisfied)  
| Requirement         | How it is satisfied                                          |
|---------------------|--------------------------------------------------------------|
| Performance         | Real-time processing (>15 FPS) on normal laptop              |
| Usability           | No mouse/keyboard needed after start – just show hand        |
| Reliability         | Works in hostel/room lighting conditions                    |
| Resource Efficiency | Runs smoothly on CPU (no GPU required)                       |
| Error Handling      | Gracefully handles “no hand detected” cases                  |
| Maintainability     | Clean, modular, well-commented code with proper classes      |

**100% Original Work** – Dataset, implementation, documentation, and design completely done by me as per VITyarthi flipped-course guidelines.

**Prince**  
VIT Bhopal 
November 2025
