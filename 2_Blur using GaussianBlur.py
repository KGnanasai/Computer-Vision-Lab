import cv2
image_path = "D:/PICKS/IMG_20221128_161703_652 - Copy.jpg"
image = cv2.imread(image_path)
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()	


