import winsound

def trigger_alert(state):
    """
    Trigger an audio alert if driver is drowsy.
    """
    if state == "drowsy":
        print("⚠️ ALERT: Driver Drowsy!")
        try:
            # Beep: frequency=1000Hz, duration=500ms
            winsound.Beep(1000, 500)
        except RuntimeError:
            print("Beep not supported on this system.")

