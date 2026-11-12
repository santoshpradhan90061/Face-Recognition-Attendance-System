import cv2

# Load face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Check model
if face_cascade.empty():
    print("Error: Face detection model not loaded!")
    exit()

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Webcam not found!")
    exit()

print("Face Detection Started!")
print("Press Q to stop.")

while True:
    success, frame = camera.read()

    if not success:
        print("Unable to read webcam.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame, (x, y), (x + w, y + h), (0, 255, 0), 2
        )

        cv2.putText(
            frame, "Face Detected", (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
        )

    cv2.imshow("Face Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()