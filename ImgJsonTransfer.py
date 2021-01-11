from sys import argv
import base64
from base64 import b64encode
from json import dumps
import cv2

ENCODING = 'utf-8'  # 指定编码形式
SCRIPT_NAME, IMAGE_NAME, JSON_NAME = argv  # 获得文件名参数


def img2string(img_name):
    with open(img_name, 'rb') as jpg_file:
        byte_content = jpg_file.read()
        base64_bytes = b64encode(byte_content)
        base64_string = base64_bytes.decode(ENCODING)
        return base64_string


def string2img(img_string,saved_img_name):
    image_data = base64.b64decode(img_string)
    with open(saved_img_name, 'wb') as jpg_file:
        jpg_file.write(image_data)
