class AgenticAI:
    def __init__(self, alert_system):
        self.alert_system = alert_system
        self.state = "awake"
        self.frame_counter = 0
        self.max_frames = {"warning": 15, "critical": 30}

    def decide(self, avg_ear, threshold=0.25):
        if avg_ear < threshold:
            self.frame_counter += 1

            if self.state == "awake" and self.frame_counter > self.max_frames["warning"]:
                self.state = "warning"
                self.alert_system.soft_alert()

            elif self.state == "warning" and self.frame_counter > self.max_frames["critical"]:
                self.state = "critical"
                self.alert_system.loud_alert()
                self.alert_system.notify_contact()

        else:
            if self.state != "awake":
                self.alert_system.reset_alerts()
            self.state = "awake"
            self.frame_counter = 0

        return self.state  # useful for overlay