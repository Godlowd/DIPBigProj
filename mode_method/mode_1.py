import numpy as np
import cv2


def blur(img):
    img = cv2.blur(img, (3, 3))
    return img


def sharpen(img):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv2.filter2D(img, -1, kernel=kernel)
    return dst
