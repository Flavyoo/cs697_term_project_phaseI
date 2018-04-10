import os
import cv2 as cv

t = []
s = "/Users/Nikith/Desktop/crater_data/images/tile3_24/non-crater"
t = os.listdir(s)
for t1 in t:
    img = cv.imread("/Users/Nikith/Desktop/crater_data/images/tile3_24/non-crater/"+t1)
    img = cv.resize(img, (200, 200))
    cv.normalize(img, img, 0, 255, cv.NORM_MINMAX)
    cv.imwrite('normalized_images/non-crater/'+t1,img)


t = []
s = "/Users/Nikith/Desktop/crater_data/images/tile3_24/crater"
t = os.listdir(s)
for t1 in t:
    img = cv.imread("/Users/Nikith/Desktop/crater_data/images/tile3_24/crater/"+t1)
    img = cv.resize(img, (200, 200))
    cv.normalize(img, img, 0, 255, cv.NORM_MINMAX)
    cv.imwrite('normalized_images/crater/'+t1,img)
    
    