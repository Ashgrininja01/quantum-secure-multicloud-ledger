import cv2
import hashlib

KEY_PATH = "biometric/biometric.key"

def authenticate_face():
    cam = cv2.VideoCapture(0)
    print("Face authentication: press 'q' to verify.")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Authenticate Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    current = hashlib.sha256(gray.tobytes()).digest()

    with open(KEY_PATH, "rb") as f:
        stored = f.read()

    if current == stored:
        print("Face authentication successful.")
        return True
    else:
        print("Face authentication failed.")
        return False

if __name__ == "__main__":
    authenticate_face()

