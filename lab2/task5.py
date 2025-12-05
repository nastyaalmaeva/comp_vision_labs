import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = (170, 120, 70)
    upper_red = (180, 255, 255)
    red = cv2.inRange(hsv, lower_red, upper_red)

    kernel = np.ones((3, 3), np.uint8)

    eroded = cv2.erode(red, kernel, iterations=1) #уменьшить белые области
    dilated = cv2.dilate(red, kernel, iterations=1) #увеличить белые области

    cv2.imshow('Eroded', eroded)
    cv2.imshow('Dilated', dilated)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()