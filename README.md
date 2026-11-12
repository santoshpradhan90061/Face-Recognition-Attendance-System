
# Face Recognition Attendance System

## Project Overview
The Face Recognition Attendance System is a Python-based application that uses computer vision to recognize registered faces and automatically record attendance with the date and time.

## Technologies Used
- Python
- OpenCV
- OpenCV Contrib
- NumPy
- CSV
- Visual Studio Code

## Features
1. Face Detection using Haar Cascade.
2. Face Registration using webcam.
3. Face Recognition using LBPH algorithm.
4. Automatic Attendance Recording.
5. Prevents duplicate attendance on the same day.
6. View Attendance Records.
7. Main Menu for easy navigation.

## Project Structure
```text
Face-Recognition-Attendance-System/
├── dataset/
├── main.py
├── register_face.py
├── recognize_face.py
├── attendance.py
├── view_attendance.py
├── menu.py
└── README.md
```

## Installation

Install the required packages:

```bash
pip install opencv-contrib-python==4.13.0.92 numpy
```

## How to Run

1. Open the project folder in VS Code.
2. Activate the virtual environment.
3. Run:

```bash
python menu.py
```

## Menu Options
1. Register New Face
2. Recognize Face
3. Mark Attendance
4. View Attendance
5. Exit

## Author
Santosh Pradhan

## Note
This is an educational prototype. Face registration and recognition should be used only with participants' consent. Recognition results may be inaccurate and should be checked before relying on attendance records.
