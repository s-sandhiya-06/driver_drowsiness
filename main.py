import cv2
from capture import init_camera, get_frame
from detector import detect_features
from analyzer import analyze_state
from alert import trigger_alert
from logger import log_event
from metrics import update_metrics, report_metrics

def main():
    cap = init_camera()

    while True:
        frame = get_frame(cap)
        features = detect_features(frame)
        state = analyze_state(features)

        trigger_alert(state)
        log_event(state)
        update_metrics(state)

        # Draw detections for visualization
        for (x, y, w, h) in features["faces"]:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        for (ex, ey, ew, eh) in features["eyes"]:
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        cv2.imshow("Driver Monitor", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    report_metrics()

if __name__ == "__main__":
    main()

