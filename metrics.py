total_frames = 0
drowsy_count = 0

def update_metrics(state):
    """
    Update counters based on driver state.
    """
    global total_frames, drowsy_count
    total_frames += 1
    if state == "drowsy":
        drowsy_count += 1

def report_metrics():
    """
    Print summary at end of run.
    """
    print("\n=== Metrics Report ===")
    print(f"Total Frames Processed: {total_frames}")
    print(f"Drowsy Alerts: {drowsy_count}")
    if total_frames > 0:
        print(f"Percentage Drowsy: {(drowsy_count/total_frames)*100:.2f}%")

