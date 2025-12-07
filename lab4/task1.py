import cv2

def show_gaussian_blur(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error loading image:", image_path)
        return

    blur = cv2.GaussianBlur(img, (7, 7), sigmaX=3)

    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.imshow("Original", img)

    cv2.namedWindow("Gaussian Blur", cv2.WINDOW_NORMAL)
    cv2.imshow("Gaussian Blur", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


show_gaussian_blur("C:/Users/nastya/Desktop/images/img3.jpg")