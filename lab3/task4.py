import cv2
import numpy as np

def gaussian_kernel(size, sigma):
    kernel = np.zeros((size, size), np.float32)
    center = size // 2
    for x in range(size):
        for y in range(size):
                kernel[x, y] = np.exp(-((x - center)**2 + (y - center)**2) / (2 * sigma**2)) / (2 * np.pi * sigma**2)
    kernel /= np.sum(kernel)
    return kernel

def apply_gaussian_blur(img, size, sigma):
    kernel = gaussian_kernel(size, sigma)
    h, w = img.shape
    pad = size // 2
    result = np.zeros_like(img, dtype=np.float32)

    for i in range(pad, h - pad):
        for j in range(pad, w - pad):
            region = img[i - pad:i + pad + 1, j - pad:j + pad + 1]
            result[i, j] = np.sum(region * kernel)
    return np.clip(result, 0, 255).astype(np.uint8)

img = cv2.imread("C:/Users/nastya/Desktop/images/img1.jpg", cv2.IMREAD_GRAYSCALE)

blur1 = apply_gaussian_blur(img, size=3, sigma=1)
blur2 = apply_gaussian_blur(img, size=7, sigma=2)
blur3 = apply_gaussian_blur(img, size=7, sigma=3)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)

cv2.namedWindow("Blur 3x3, sigma=1", cv2.WINDOW_NORMAL)
cv2.imshow("Blur 3x3, sigma=1", blur1)

cv2.namedWindow("Blur 7x7, sigma=2", cv2.WINDOW_NORMAL)
cv2.imshow("Blur 7x7, sigma=2", blur2)

cv2.namedWindow("Blur 7x7, sigma=3", cv2.WINDOW_NORMAL)
cv2.imshow("Blur 7x7, sigma=3", blur3)

cv2.waitKey(0)
cv2.destroyAllWindows()