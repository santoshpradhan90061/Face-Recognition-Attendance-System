import cv2
import os
import csv
import numpy as np
from datetime import datetime

# Load face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Create face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

dataset_path = "dataset"
faces = []
labels = []
names = {}
label_id = 0

# Load registered faces
for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_folder):
        continue

    names[label_id] = person_name

    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)
        image = cv2.imread(image_path)

        if image is None:
            continue

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (200, 200))

        faces.append(gray)
        labels.append(label_id)

    label_id += 1

if not faces:
    print("No registered faces found!")
    exit()

# Train the recognizer
recognizer.train(faces, np.array(labels))
print("Face recognition model trained!")

# Create attendance file if it does not exist
file_name = "attendance.csv"

if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time"])

# Record attendance only once per day
def mark_attendance(name):
    today = datetime.now().strftime("%Y-%m-%d")

    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2 and row[0] == name and row[1] == today:
                return False

    current_time = datetime.now().strftime("%H:%M:%S")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, today, current_time])

    return True

# Start webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Webcam not found!")
    exit()

print("Attendance System Started!")
print("Press Q to stop.")

marked_today = set()

while True:
    success, frame = camera.read()

    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_faces = face_cascade.detectMultiScale(
        gray, 1.1, 5, minSize=(80, 80)
    )

    for (x, y, w, h) in detected_faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label, confidence = recognizer.predict(face)

        if confidence < 70:
            name = names[label]
            color = (0, 255, 0)

            if name not in marked_today:
                if mark_attendance(name):
                    print(f"Attendance marked for {name}")
                else:
                    print(f"{name}'s attendance already exists today.")

                marked_today.add(name)

        else:
            name = "Unknown"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(
            frame, name, (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2
        )

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print("Attendance system closed.")