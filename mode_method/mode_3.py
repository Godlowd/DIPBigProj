import cv2


# 直方图均衡化
def equalizeHist(img):
    converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    (h, l, s) = cv2.split(converted_img)
    equalized_l = cv2.equalizeHist(l)
    converted_img = cv2.merge((h, equalized_l, s))
    img = cv2.cvtColor(converted_img, cv2.COLOR_HLS2BGR)
    return img
