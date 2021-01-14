import cv2


def eraser(img, original_img, x, y, erase_scale):
    img[y - erase_scale:y + erase_scale, x - erase_scale:x + erase_scale] = original_img[y - erase_scale:y + erase_scale, x - erase_scale:x + erase_scale]
