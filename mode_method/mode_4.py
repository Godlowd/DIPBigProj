import cv2
import numpy as np


def flood_fill(img, x, y, scale, color=(0, 0, 255)):
    cv2.floodFill(img, None, (x, y), color, (scale, scale, scale), (scale, scale, scale), 4)
    return img


def bag(img):
    color = (0, 0, 255)
    lower = np.array([0, 253, 253])
    upper = np.array([3, 255, 255])
    """对img_flood上的红色区域进行凸包运算并标记"""
    # global hull
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    # 寻找凸包并绘制凸包（轮廓）
    for cnt in contours:
        hull = cv2.convexHull(cnt)
        length = len(hull)
        # 如果凸包点集中的点个数大于5
        if length > 5:
            # 绘制图像凸包的轮廓
            for i in range(length):
                cv2.line(img, tuple(hull[i][0]), tuple(hull[(i + 1) % length][0]), (0, 255, 0), 1)
            M = cv2.moments(cnt)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # point = (cX, cY)
            cv2.circle(img, (cX, cY), 2, (0, 255, 255), -1)
