import winsound

class AlertSystem:
    def soft_alert(self):
        print("⚠ Soft Alert: Please wake up!")
        winsound.Beep(1000, 300)

    def loud_alert(self):
        print("🚨 LOUD ALERT: WAKE UP NOW!")
        winsound.Beep(1500, 700)

    def notify_contact(self):
        print("📲 Notifying emergency contact... (simulation)")

    def reset_alerts(self):
        print("✅ Alerts reset, driver is awake.")