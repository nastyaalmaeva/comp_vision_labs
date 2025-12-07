import cv2
import numpy as np
import os


def non_max_suppression(magnitude, angle):
    angle = angle * 180 / np.pi
    angle[angle < 0] += 180

    h, w = magnitude.shape
    suppressed = np.zeros((h, w), dtype=np.float32)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            q = r = 0

            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                q = magnitude[i, j + 1]
                r = magnitude[i, j - 1]
            elif 22.5 <= angle[i, j] < 67.5:
                q = magnitude[i - 1, j + 1]
                r = magnitude[i + 1, j - 1]
            elif 67.5 <= angle[i, j] < 112.5:
                q = magnitude[i - 1, j]
                r = magnitude[i + 1, j]
            else:
                q = magnitude[i - 1, j - 1]
                r = magnitude[i + 1, j + 1]

            if magnitude[i, j] >= q and magnitude[i, j] >= r:
                suppressed[i, j] = magnitude[i, j]

    return suppressed


def hysteresis(result, weak=75, strong=255):
    h, w = result.shape
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if result[i, j] == weak:
                if np.any(result[i - 1:i + 2, j - 1:j + 2] == strong):
                    result[i, j] = strong
                else:
                    result[i, j] = 0
    return result


def run_small_experiment_set(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error loading image")
        return

    os.makedirs("Results", exist_ok=True)

    kernels = [3, 5]
    sigmas = [0.5, 1.2]
    low_vals = [5, 10]
    high_vals = [15, 20]

    exp_id = 1

    for k in kernels:
        for sigma in sigmas:

            blur = cv2.GaussianBlur(img, (k, k), sigmaX=sigma)

            sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0)
            sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1)

            magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
            angle = np.arctan2(sobel_y, sobel_x)

            suppressed = non_max_suppression(magnitude, angle)
            max_grad = suppressed.max()

            for low, high in zip(low_vals, high_vals):

                low_t = max_grad * (low / 100)
                high_t = max_grad * (high / 100)

                strong = 255
                weak = 75

                result = np.zeros_like(suppressed, dtype=np.uint8)
                strong_idx = suppressed >= high_t
                weak_idx = (suppressed >= low_t) & (suppressed < high_t)

                result[strong_idx] = strong
                result[weak_idx] = weak

                result = hysteresis(result)

                filename = f"Results/exp_{exp_id}_k{k}_s{sigma}_low{low}_high{high}.png"
                cv2.imwrite(filename, result)

                print(f"[{exp_id}] kernel={k}, sigma={sigma}, low={low}, high={high}")

                exp_id += 1


run_small_experiment_set("C:/Users/nastya/Desktop/images/img3.jpg")