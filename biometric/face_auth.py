import cv2
import face_recognition
import numpy as np

KEY_PATH = "biometric/biometric.key.npy"

def authenticate_face():
    stored = np.load(KEY_PATH)

    cam = cv2.VideoCapture(2)
    print("Face authentication started")

    while True:
        ret, frame = cam.read()
        if not ret:
            continue

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)

        if len(boxes) == 1:
            encoding = face_recognition.face_encodings(rgb, boxes)[0]
            dist = np.linalg.norm(stored - encoding)
            print(f"Distance: {dist:.3f}")

            if dist < 0.75:
                print("Face authentication successful")
                break
            else:
                print("Face authentication failed")

        cv2.imshow("Auth Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    authenticate_face()
