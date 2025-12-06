import numpy as np

def gaussian_kernel(size, sigma):

    kernel = np.zeros((size, size), np.float32)

    center = size // 2

    for x in range(size):
        for y in range(size):
            kernel[x, y] = np.exp(-((x - center)**2 + (y - center)**2) / (2 * sigma**2)) / (2 * np.pi * sigma**2)
    print(np.sum(kernel))
    return kernel

for s in [3, 5, 7]:
    print(f"\nKernel size: {s}x{s}")
    print(gaussian_kernel(s, sigma=1))