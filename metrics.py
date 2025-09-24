class Metrics:
    def __init__(self):
        self.frames_processed = 0
        self.alerts_triggered = 0

    def update(self):
        self.frames_processed += 1

    def alert(self):
        self.alerts_triggered += 1

    def report(self):
        return {
            "frames_processed": self.frames_processed,
            "alerts_triggered": self.alerts_triggered
        }
