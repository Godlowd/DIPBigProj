from tkinter import *
import tkinter.filedialog
import cv2
import numpy as np


def AdaptProcess(src, i, j, minSize, maxSize):
    filter_size = minSize

    kernelSize = filter_size // 2
    rio = src[i - kernelSize:i + kernelSize + 1, j - kernelSize:j + kernelSize + 1]
    minPix = np.min(rio)
    maxPix = np.max(rio)
    medPix = np.median(rio)
    zxy = src[i, j]

    if (medPix > minPix) and (medPix < maxPix):
        if (zxy > minPix) and (zxy < maxPix):
            return zxy
        else:
            return medPix
    else:
        filter_size = filter_size + 2
        if filter_size <= maxSize:
            return AdaptProcess(src, i, j, filter_size, maxSize)
        else:
            return medPix


def adapt_meadian_filter(img, minsize, maxsize):
    borderSize = maxsize // 2

    src = cv2.copyMakeBorder(img, borderSize, borderSize, borderSize, borderSize, cv2.BORDER_REFLECT)

    for m in range(borderSize, src.shape[0] - borderSize):
        for n in range(borderSize, src.shape[1] - borderSize):
            src[m, n] = AdaptProcess(src, m, n, minsize, maxsize)

    dst = src[borderSize:borderSize + img.shape[0], borderSize:borderSize + img.shape[1]]
    return dst


def sharpen(img):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv2.filter2D(img, -1, kernel=kernel)
    return dst


# 预处理
def preprocess(original_img):
    # 中值滤波去噪声
    temp_img = adapt_meadian_filter(original_img, 1, 10)
    # 锐化提升品质
    temp_img = sharpen(temp_img)
    return temp_img


filename = tkinter.filedialog.askopenfilename()
if filename != '':
    print(filename)
    img = cv2.imread(filename, 0)
    img = preprocess(img)
    cv2.imshow("original", img)
    cv2.waitKey(0)
else:
    print("nothing")
