import os
import cv2 as cv
import random
#place this program in images folder to make it work

def randomscaling(srcd,destd):
    t = []
    s = srcd+"/non-crater/"
    t = os.listdir(s)
    z = 0;
    for t1 in t:
        ran=random.randint(10,101)
        
        img = cv.imread(s+t1)
        img = cv.resize(img, (ran, ran))
        cv.normalize(img, img, 0, 255, cv.NORM_MINMAX)
        cv.imwrite(destd+'/non-crater/'+'norm'+str(z)+'.jpg',img)
        z+=1;

    t = []
    s = srcd+"/crater/"
    t = os.listdir(s)
    z= 0
    for t1 in t:
        ran=random.randint(10,101)
        img = cv.imread(s+t1)
        img = cv.resize(img, (ran, ran))
        cv.normalize(img, img, 0, 255, cv.NORM_MINMAX)
        cv.imwrite(destd+'/crater/'+'norm'+str(z)+'.jpg',img)
        z+=1
#relative adrres of directory that contains crater and non craters(inputs)
#it rotates and scales each image randomly
#it should be in image directory if u want to use it without changes
srcd="tile3_24"
destd='rannorm'
randomscaling(srcd,destd)