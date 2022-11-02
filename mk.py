import cv2
cap= cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #инверсия цвета
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# градации серого
    #ret, frame = cv2.threshold(frame, 150, 200, 10)#трешхолд, все что ярче 255 что темнее 0 
   # cv2.putText(frame, "текст", (1500, 3600),cv2.FONT_HERSHEY_SIMPLEX, 15, (30, 105, 210), 40) #

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, (0, 161, 118), (185, 242, 197))
    thresh = cv2.GaussianBlur(thresh, (5, 5), 2)
    conts, heir = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if conts:
        cv2.drawContours(frame, conts, -1, (0, 255, 0), 2)
        print(conts)


    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows