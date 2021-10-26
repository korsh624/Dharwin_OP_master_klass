import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, (0, 161, 118), (185, 242, 197))
    thresh = cv2.GaussianBlur(thresh, (5, 5), 2)
    conts, heir = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if conts:
        cv2.drawContours(frame, conts, -1, (0, 255, 0), 2)
        print(conts)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows