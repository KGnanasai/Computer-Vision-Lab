#To Perform basic Image Handling and processing operations on the image. Read an image in python and Convert an Image to Grayscale
import cv2
image_path = "D:/PICKS/IMG_20221128_161703_652 - Copy.jpg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
