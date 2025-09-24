import cv2

class VideoCapture:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src)

    def read(self):
        if not self.cap.isOpened():
            raise Exception("Camera not accessible")
        ret, frame = self.cap.read()
        return ret, frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
