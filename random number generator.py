import cv2 as cv
import hashlib
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, image = cap.read()

    hash_obj = hashlib.sha256(image.tobytes())

    hash_degeri = hash_obj.hexdigest()

    cv.imshow('image', image)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv.destroyAllWindows()
