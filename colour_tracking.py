import cv2
import numpy as np

cameraman=cv2.VideoCapture(0,cv2.CAP_DSHOW)#start the webcam
lower_blue=np.array([100,150,0])
upper_blue=np.array([140,255,255])
while True:
    ret, frame = cameraman.read()
    if not ret:
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a binary mask where blue is 1
    mask = cv2.inRange(hsv, lower_blue, upper_blue)



    # Find contours from the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, "Blue Object", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

    # Show both the mask and result
    cv2.imshow("Mask", mask)
    cv2.imshow("Tracked Object", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cameraman.release()
cv2.destroyAllWindows()
