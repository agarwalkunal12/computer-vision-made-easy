# Lesson 1: An image is just a grid of numbers

Code for the lesson at [computervisionmadeeasy.com](https://computervisionmadeeasy.com/lessons/an-image-is-just-numbers.html).

Loads a photo as a grayscale grid, prints its shape and data type, reads one pixel, and shows the difference between OpenCV’s clipping addition and NumPy’s wrapping addition.

```bash
python lesson1.py                 # uses a built-in test image
python lesson1.py path/to/photo.jpg
```

Expected output with the built-in test image (the last numbers depend on your image):

```
shape: (480, 640)
dtype: uint8
...
cv2.add(img, 100) there: 255
img + 100 there:         44
img[row, col] + 100:     44 (warning: overflow encountered in scalar add)
```

**What to notice:** `cv2.add` stops at 255. Plain `+` on a `uint8` array wraps around past 255 with no warning; on a single pixel it wraps too, but NumPy warns you.
