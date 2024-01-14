import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    result = cv.medianBlur(frame, ksize=7)
    cv.imshow('frame', result)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()