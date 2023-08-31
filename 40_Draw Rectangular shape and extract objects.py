#Draw Rectangular shape and extract objects

import cv2
img = cv2.imread("D:/ʀᴏᴡᴅʏ ʙᴏʏs/IMG_3329.JPG")
x, y = 100, 100
width, height = 700, 650
roi = img[y:y+height, x:x+width]
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
