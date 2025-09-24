import cv2
from capture import VideoCapture
from detector import FaceMeshDetector
from analyzer import DrowsinessAnalyzer
from alert import AlertSystem
from agent import AgenticAI

EYE_INDICES = {
    "left": [33, 160, 158, 133, 153, 144],
    "right": [362, 385, 387, 263, 373, 380]
}

def main():
    print("🚗 Driver Drowsiness Detection Started...")

    capture = VideoCapture()
    detector = FaceMeshDetector()
    analyzer = DrowsinessAnalyzer(EYE_INDICES)
    alert_system = AlertSystem()
    agent = AgenticAI(alert_system)

    while True:
        ret, frame = capture.read()
        if not ret:
            break

        landmarks = detector.detect(frame)
        if landmarks:
            detector.draw_landmarks(frame, landmarks)
            ear, avg_ear = analyzer.analyze(landmarks.landmark, frame.shape)
            state = agent.decide(avg_ear, threshold=analyzer.threshold)

            # 🟢 Overlay EAR and state on video feed
            cv2.putText(frame, f"EAR: {avg_ear:.3f}", (30, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(frame, f"State: {state}", (30, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (0, 0, 255) if state != "awake" else (0, 255, 0), 2)

        cv2.imshow("Driver Monitor", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    print("✅ Program ended")

if __name__ == "__main__":
    main()