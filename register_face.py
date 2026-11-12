import cv2
import os

# Load face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Ask for person's name
name = input("Enter person's name: ").strip()

if not name:
    print("Name cannot be empty!")
    exit()

# Create a folder for this person
person_folder = os.path.join("dataset", name)
os.makedirs(person_folder, exist_ok=True)

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Webcam not found!")
    exit()

count = 0
print("Look at the camera. Press Q to stop.")

while count < 20:
    success, frame = camera.read()

    if not success:
        print("Camera reading failed!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, 1.1, 5, minSize=(80, 80)
    )

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]

        count += 1
        image_path = os.path.join(
            person_folder, f"face_{count}.jpg"
        )
        cv2.imwrite(image_path, face)

        cv2.rectangle(
            frame, (x, y), (x+w, y+h), (0, 255, 0), 2
        )

        cv2.putText(
            frame, f"Images: {count}/20", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
        )

        break

    cv2.imshow("Face Registration", frame)

    if cv2.waitKey(300) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print(f"Registration completed. Saved {count} images for {name}.")