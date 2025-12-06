import cv2
import numpy as np

def gaussian_kernel(size, sigma):
    kernel = np.zeros((size, size), np.float32)
    center = size // 2
    for x in range(size):
        for y in range(size):
                kernel[x, y] = np.exp(-((x - center)**2 + (y - center)**2) / (2 * sigma**2)) / (2 * np.pi * sigma**2)

    return kernel

def apply_gaussian_blur(image_path, size, sigma):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    kernel = gaussian_kernel(size, sigma)
    h, w = img.shape
    pad = size // 2

    result = np.zeros_like(img, dtype=np.float32)

    for i in range(pad, h - pad):
        for j in range(pad, w - pad):
            region = img[i - pad:i + pad + 1, j - pad:j + pad + 1]
            result[i, j] = np.sum(region * kernel)

    result = np.clip(result, 0, 255).astype(np.uint8)
    return result


img = cv2.imread("C:/Users/nastya/Desktop/images/img1.jpg", cv2.IMREAD_GRAYSCALE) #"C:/Users/nastya/Desktop/images/img1.jpg"

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)

blurred = apply_gaussian_blur("C:/Users/nastya/Desktop/images/img1.jpg", size=9, sigma=5)

cv2.namedWindow("Gaussian Blur", cv2.WINDOW_NORMAL)
cv2.imshow("Gaussian Blur", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()