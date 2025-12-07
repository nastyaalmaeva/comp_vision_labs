import cv2
import numpy as np


def show_gradients(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error loading image:", image_path)
        return

    blur = cv2.GaussianBlur(img, (7, 7), sigmaX=3)

    cv2.namedWindow("Blurred", cv2.WINDOW_NORMAL)
    cv2.imshow("Blurred", blur)

    sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

    grad_length = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    grad_angle = np.arctan2(sobel_y, sobel_x)

    np.set_printoptions(precision=2, suppress=True)
    print("Gradient lenghts matrix:")
    print(grad_length)
    print("Gradient angles matrix:")
    print(grad_angle)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


show_gradients("C:/Users/nastya/Desktop/images/img3.jpg")