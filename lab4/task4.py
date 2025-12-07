import cv2
import numpy as np


def double_threshold(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error loading image:", image_path)
        return

    blur = cv2.GaussianBlur(img, (5, 5), sigmaX=1)

    sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

    magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    angle = np.arctan2(sobel_y, sobel_x) * 180 / np.pi
    angle[angle < 0] += 180

    h, w = magnitude.shape
    suppressed = np.zeros((h, w), dtype=np.float32)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            q = 0
            r = 0
            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                q = magnitude[i, j + 1]
                r = magnitude[i, j - 1]
            elif 22.5 <= angle[i, j] < 67.5:
                q = magnitude[i - 1, j + 1]
                r = magnitude[i + 1, j - 1]
            elif 67.5 <= angle[i, j] < 112.5:
                q = magnitude[i - 1, j]
                r = magnitude[i + 1, j]
            elif 112.5 <= angle[i, j] < 157.5:
                q = magnitude[i - 1, j - 1]
                r = magnitude[i + 1, j + 1]

            if magnitude[i, j] >= q and magnitude[i, j] >= r:
                suppressed[i, j] = magnitude[i, j]

    max_grad = suppressed.max()
    if max_grad == 0:
        print("Gradients not found")
        return

    high_level = max_grad / 10
    low_level = max_grad / 25

    strong = 255
    weak = 75

    result = np.zeros_like(suppressed, dtype=np.uint8)
    strong_i, strong_j = np.where(suppressed >= high_level)
    weak_i, weak_j = np.where((suppressed >= low_level) & (suppressed < high_level))

    result[strong_i, strong_j] = strong
    result[weak_i, weak_j] = weak

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if result[i, j] == weak:
                if np.any(result[i - 1:i + 2, j - 1:j + 2] == strong):
                    result[i, j] = strong
                else:
                    result[i, j] = 0

    cv2.namedWindow("Double threshold filtering", cv2.WINDOW_NORMAL)
    cv2.imshow("Double threshold filtering", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


double_threshold("C:/Users/nastya/Desktop/images/img3.jpg")