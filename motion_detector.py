import cv2
import numpy as np

def detect_motion(frame1, frame2, threshold=50000):
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    count = cv2.countNonZero(dilated)

    detected = count > threshold
    return detected, count, frame1
