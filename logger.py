import datetime

def log_event(state, logfile="drowsiness.log"):
    """
    Log driver state with timestamp.
    """
    with open(logfile, "a") as f:
        f.write(f"{datetime.datetime.now()} - {state}\n")

