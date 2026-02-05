import cv2
import hashlib
import os

OUT = "biometric/biometric.key"

def enroll_face():
    cam = cv2.VideoCapture(0)
    print("Face enrollment: press 'q' to capture.")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Enroll Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    key = hashlib.sha256(gray.tobytes()).digest()

    os.makedirs("biometric", exist_ok=True)
    with open(OUT, "wb") as f:
        f.write(key)

    print("Face enrolled. Biometric key stored (derived, no raw image).")

if __name__ == "__main__":
    enroll_face()

