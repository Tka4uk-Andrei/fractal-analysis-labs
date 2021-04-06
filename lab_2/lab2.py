import cv2
import numpy as np


def getRedPart(img):
    img_copy = img.copy()
    img_copy[:, :, 1] = np.zeros([img_copy.shape[0], img_copy.shape[1]])
    img_copy[:, :, 2] = np.zeros([img_copy.shape[0], img_copy.shape[1]])

    return img_copy


def getGreenPart(img):
    img_copy = img.copy()
    img_copy[:, :, 0] = np.zeros([img_copy.shape[0], img_copy.shape[1]])
    img_copy[:, :, 2] = np.zeros([img_copy.shape[0], img_copy.shape[1]])

    return img_copy


def getBluePart(img):
    img_copy = img.copy()
    img_copy[:, :, 0] = np.zeros([img_copy.shape[0], img_copy.shape[1]])
    img_copy[:, :, 1] = np.zeros([img_copy.shape[0], img_copy.shape[1]])

    return img_copy


img_name = 'img1.jpg'
img = cv2.imread(img_name)

red_img   = getRedPart(img)
blue_img  = getBluePart(img)
green_img = getGreenPart(img)

cv2.imwrite("red_"   + img_name, red_img)
cv2.imwrite("blue_"  + img_name, blue_img)
cv2.imwrite("green_" + img_name, green_img)
