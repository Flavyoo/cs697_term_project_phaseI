"""
Nikith AnupKumar

This program reads crater images from their respective locations and scales them
to be 200 by 200 pixels.
"""
import os
import cv2 as cv
from paths import CRATER_SCALED_PATH, NON_CRATER_SCLALED_PATH
THIS_DIR = os.path.dirname(__file__)
TILE3_24_CRATER = os.path.join(THIS_DIR, '../tile3_24/crater/')
TILE3_24_NON_CRATER = os.path.join(THIS_DIR, '../tile3_24/non-crater/')
CRATER = os.path.join(THIS_DIR, 'crater/')
NON_CRATER = os.path.join(THIS_DIR, 'non-cratercrater/')

t = []
s = TILE3_24_NON_CRATER
t = os.listdir(s)
for t1 in t:
    img = cv.imread(TILE3_24_NON_CRATER+t1)
    img = cv.resize(img, (200, 200))
    cv.normalize(img, img, 0, 255, cv.NORM_MINMAX)
    cv.imwrite(NON_CRATER_SCLALED_PATH+t1,img)


t = []
s = TILE3_24_CRATER
t = os.listdir(s)
for t1 in t:
    img = cv.imread(TILE3_24_CRATER +t1)
    img = cv.resize(img, (200, 200))
    cv.normalize(img, img, 0, 255, cv.NORM_MINMAX)
    cv.imwrite(CRATER_SCALED_PATH+t1,img)
