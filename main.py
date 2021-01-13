from tkinter import *
import tkinter.filedialog
import cv2
import numpy as np
from mode_method.mode_0 import *
from mode_method.mode_1 import *
from mode_method.mode_2 import *
from mode_method.mode_3 import equalizeHist
# 软件工作模式
"""
mode 0：给照片涂抹马赛克，加号增大马赛克范围，减号缩小
"""
mode = 0
current_img = None
# 仿射变换需要的变量
point1 = [0, 0]
point2 = [0, 0]
point3 = [0, 0]
point4 = [0, 0]
numberOfPoint = 0


# 鼠标回调函数
def detect_mode(event, x, y, flags, param):
    global current_img, numberOfPoint, point1, point2, point3, point4
    if mode == 0:
        if event == cv2.EVENT_LBUTTONDOWN:
            spot = (x, y)
            print(spot)
            do_mosaic(current_img, x, y, 80, 80)
            cv2.imshow("main", current_img)
        pass
    elif mode == 1:
        if event == cv2.EVENT_RBUTTONDOWN:
            current_img = blur(current_img)
            cv2.imshow("main", current_img)
        elif event == cv2.EVENT_LBUTTONDOWN:
            current_img = sharpen(current_img)
            cv2.imshow("main", current_img)
    elif mode == 2:
        if event == cv2.EVENT_LBUTTONDOWN:
            numberOfPoint = numberOfPoint + 1
            if numberOfPoint == 1:
                point1 = (x, y)
            elif numberOfPoint == 2:
                point2 = (x, y)
            elif numberOfPoint == 3:
                point3 = (x, y)
            elif numberOfPoint == 4:
                point4 = (x, y)
                point1, point2, point3, point4 = reRange(point1, point2, point3, point4)
                src_point = np.float32([point1, point2, point3, point4])
                dst_point = np.float32([[0, 0], [0, 300], [300, 300], [300, 0]])
                h = cv2.getPerspectiveTransform(src_point, dst_point)
                res = cv2.warpPerspective(img, h, (300, 300))
                cv2.imshow('affineTransform', res)

                point1 = point3 = point2 = point4 = (0, 0)
                numberOfPoint = 0
    elif mode == 3:
        if event == cv2.EVENT_LBUTTONDOWN:
            current_img = equalizeHist(current_img)
            cv2.imshow('main', current_img)
        pass


def onMouseEvent(event):
    # 监听鼠标事件
    print("MessageName:", event.MessageName)
    print("Message:", event.Message)
    print("Time:", event.Time)
    print("Window:", event.Window)
    print("WindowName:", event.WindowName)
    print("Position:", event.Position)
    print("Wheel:", event.Wheel)
    print("Injected:", event.Injected)
    print("---")

    # 返回 True 以便将事件传给其它处理程序
    # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
    # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了
    return True


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
    cv2.namedWindow('main')
    cv2.setMouseCallback('main', detect_mode)
    img = cv2.imread(filename)
    current_img = img
    # 用来恢复原图像
    original_img = img
    # do_mosaic(current_img, 377, 155, 80, 80)
    cv2.imshow("main", current_img)
    while 1:
        k = cv2.waitKey(1) & 0xFF
        if k == ord('r'):
            cv2.imshow("main", original_img)
            current_img = original_img
        elif k == ord('0'):
            mode = 0
        elif k == ord('1'):
            mode = 1
        elif k == ord('2'):
            mode = 2
        elif k == ord('3'):
            mode = 3


else:
    print("nothing")
