import cv2
import numpy as np


def non_max_suppression(image_path):
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

    if suppressed.max() > 0:
        suppressed_img = (suppressed / suppressed.max() * 255).astype(np.uint8)
    else:
        suppressed_img = suppressed.astype(np.uint8)

    cv2.namedWindow("Non-maximum suppression", cv2.WINDOW_NORMAL)
    cv2.imshow("Non-maximum suppression", suppressed_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


non_max_suppression("C:/Users/nastya/Desktop/images/img3.jpg")