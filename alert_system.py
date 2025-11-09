from datetime import datetime

def send_alert():
    """Simulate sending an emergency alert after detecting an accident."""
    alert_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{alert_time}] Accident detected! Virtual alert sent to emergency unit."
    print(message)

    # Save log
    with open("outputs/accident_log.txt", "a") as file:
        file.write(message + "\n")
