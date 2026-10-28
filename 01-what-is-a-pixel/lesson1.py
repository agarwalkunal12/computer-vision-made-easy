"""Lesson 1: An image is just a grid of numbers.

Run:  python lesson1.py                 (uses a small built-in test image)
      python lesson1.py path/to/photo.jpg

Tested with Python 3.12, NumPy 2.5.4 and OpenCV 5.0.0.
"""
import sys
import warnings

import cv2
import numpy as np


def load_grayscale(path=None):
    """Decode a photo file into a grayscale grid, or build a test image if no path is given."""
    if path is None:
        # A 480 x 640 test image: a left-to-right fade from dark to bright,
        # so it contains pixels near 200 for the overflow demo below.
        return np.tile(np.linspace(0, 255, 640).astype(np.uint8), (480, 1))
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        sys.exit(f"Could not open {path!r}. Check the path and that it is an image file.")
    return img


def main():
    img = load_grayscale(sys.argv[1] if len(sys.argv) > 1 else None)

    # The grid: rows first, then columns (height before width)
    print("shape:", img.shape)      # (rows, columns)
    print("dtype:", img.dtype)      # uint8: whole numbers 0 to 255, stored in 8 bits

    # One pixel, by its address: row 10, column 44
    print("img[10, 44] =", img[10, 44])

    # Find a pixel that is exactly 200 (or the closest one) to make the overflow visible
    row, col = np.unravel_index(np.abs(img.astype(int) - 200).argmin(), img.shape)
    print(f"\nPixel at row {row}, column {col} is {img[row, col]}")

    brighter = cv2.add(img, 100)    # OpenCV clips: 200 + 100 gives 255
    oops = img + 100                # NumPy wraps:  200 + 100 gives 44, silently
    print("cv2.add(img, 100) there:", brighter[row, col])
    print("img + 100 there:        ", oops[row, col])

    # A single pixel also wraps, but NumPy prints a warning this time
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        single = img[row, col] + 100
    print("img[row, col] + 100:    ", single, f"(warning: {caught[0].message})" if caught else "(no warning)")


if __name__ == "__main__":
    main()
