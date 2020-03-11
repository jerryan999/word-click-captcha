# -*- coding:UTF-8 -*-
import cv2
import numpy as np


def match_img(img_mp,template):
    img_gray = cv2.cvtColor(img_mp,cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    maxLoc = cv2.minMaxLoc(res)
    print(maxLoc)
    threshold = maxLoc[1]
    loc = np.where(res>=threshold)
    return loc


ap_path='00001.jpg'    # 模板图片

template = cv2.imread(ap_path, 0)
template01 = template[350:384,6:36]  # 01
# template02 = template[4:28, 229:252]  # 02
# template03 = template[4:28, 253:279]  # 03
cv2.imshow('template', template)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('template01', template01)
cv2.waitKey(0)
cv2.destroyAllWindows()


img_mp = cv2.imread(ap_path)[0:340,:]  
cv2.imshow('img_mp', img_mp)
cv2.waitKey(0)
cv2.destroyAllWindows()
loc1 = match_img(img_mp, template01)
# loc2 = match_img(img_mp, template02)
# loc3 = match_img(img_mp, template03)
w1, h1 = template01.shape[::-1]
# w2, h2 = template02.shape[::-1]
# w3, h3 = template03.shape[::-1]
for pt in zip(*loc1[::-1]):
    cv2.rectangle(img_mp, pt, (pt[0] + w1, pt[1] + h1), (0,0,255), 2)
# for pt in zip(*loc2[::-1]):
    # cv2.rectangle(img_mp, pt, (pt[0] + w1, pt[1] + h1), (0,255,255), 2)
# for pt in zip(*loc3[::-1]):
    # cv2.rectangle(img_mp, pt, (pt[0] + w1, pt[1] + h1), (255,0,0), 2)
cv2.imshow('Detected', img_mp)
cv2.waitKey(0)
cv2.destroyAllWindows()
