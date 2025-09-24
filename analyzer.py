# Analyzer: checks if driver is drowsy based on eye closure

EYE_CLOSED_THRESHOLD = 15  # consecutive frames with no eyes detected
closed_counter = 0

def analyze_state(features):
    """
    Analyze the features and return state: "alert" or "drowsy"
    """
    global closed_counter

    if len(features["eyes"]) == 0:   # no eyes detected
        closed_counter += 1
    else:
        closed_counter = 0

    if closed_counter >= EYE_CLOSED_THRESHOLD:
        return "drowsy"
    return "alert"

