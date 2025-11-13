import cv2

img1 = cv2.imread(r'C:/Users/nastya/Desktop/images/img1.jpg')
img2 = cv2.imread(r'C:/Users/nastya/Desktop/images/img1.jpg')

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.namedWindow('image_hsv', cv2.WINDOW_NORMAL)

cv2.imshow('image',img1)

hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
cv2.imshow('image_hsv', hsv)

print("Нажмите любую клавишу для закрытия всех окон...")
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()