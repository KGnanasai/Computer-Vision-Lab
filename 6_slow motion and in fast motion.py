import cv2
import numpy as np
cap = cv2.VideoCapture("D:/ROWDY BOYS/73cc99d923fb4ebd84167483642e4dc7.mp4")
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
