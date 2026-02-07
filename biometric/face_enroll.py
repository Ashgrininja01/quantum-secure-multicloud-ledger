import cv2
import face_recognition
import numpy as np
import os

OUT = "biometric/biometric.key"

def enroll_face():
    cam = cv2.VideoCapture(2)
    encodings = []

    print("Face enrollment started")
    print("Look straight at the camera. Capturing 10 samples...")

    while len(encodings) < 10:
        ret, frame = cam.read()
        if not ret:
            continue

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)

        if len(boxes) == 1:
            encoding = face_recognition.face_encodings(rgb, boxes)[0]
            encodings.append(encoding)
            print(f"Captured {len(encodings)}/10")

        cv2.imshow("Enroll Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    if len(encodings) < 5:
        print("Enrollment failed: insufficient samples")
        return

    biometric_key = np.mean(encodings, axis=0)

    os.makedirs("biometric", exist_ok=True)
    np.save(OUT, biometric_key)

    print("Face enrolled successfully (averaged embedding).")

if __name__ == "__main__":
    enroll_face()
