import cv2

# Загрузка изображений
img1 = cv2.imread(r'C:/Users/nastya/Desktop/images/img1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'C:/Users/nastya/Desktop/images/img2.png', cv2.IMREAD_UNCHANGED)
img3 = cv2.imread(r"C:/Users/nastya/Desktop/images/img3.webp", cv2.IMREAD_COLOR)

# Создание окон с разными именами
cv2.namedWindow('Image 1', cv2.WINDOW_NORMAL)
cv2.namedWindow('Image 2', cv2.WINDOW_NORMAL)
cv2.namedWindow('Image 3', cv2.WINDOW_NORMAL)

# Отображение изображений в разных окнах
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Image 3', img3)

print("Нажмите любую клавишу для закрытия всех окон...")
cv2.waitKey(0)
cv2.destroyAllWindows()