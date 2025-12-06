import numpy as np

def gaussian_kernel(size, sigma):
    kernel = np.zeros((size, size), np.float64)
    center = size // 2

    for x in range(size):
        for y in range(size):
                kernel[x, y] = np.exp(-((x - center)**2 + (y - center)**2) / (2 * sigma**2)) / (2 * np.pi * sigma**2)

    kernel /= np.sum(kernel)
    return kernel

for s in [3, 5, 7]:
    mat = gaussian_kernel(s, sigma=1)
    print(f"\nKernel Size: {s}x{s}")
    print(mat)
    print("Sum of elements:", np.sum(mat))