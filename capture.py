import cv2

def init_camera():
    """Initialize webcam and return capture object."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Error: Could not open webcam.")
    return cap

def get_frame(cap):
    """Grab a frame from an already opened capture object."""
    ret, frame = cap.read()
    if not ret:
        raise Exception("Error: Failed to capture frame.")
    return frame

