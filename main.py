import cv2
import numpy as np
from datetime import datetime
from alert_system import send_alert
from utils.motion_detector import detect_motion

print("\n🚗 AI-Based Accident Detection and Alert System (v1.2)\n")

cap = cv2.VideoCapture("sample_videos/example_accident.mp4")

ret, frame1 = cap.read()
ret, frame2 = cap.read()

accident_detected = False

while cap.isOpened():
    detected, diff_count, frame_processed = detect_motion(frame1, frame2)

    if detected and not accident_detected:
        accident_detected = True
        print("⚠️ Accident Detected! Sending Alert...")
        send_alert()
        
    cv2.imshow("Detection Feed", frame_processed)
    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret or cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
