

import argparse
import time
import cv2
import imutils
 
 
 
 
 
 
 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
x = []
with open('gt_tile3_24.csv','rb') as file:
	for row in file:
		entry = map(int,row.strip('\n').split(','))
		x+=[entry]
l=1
for i in x:
	cv2.circle(image,(i[0],i[1]), i[2], (0,255,255), 2)
	
	
cv2.imshow("Window", image)
cv2.waitKey(0)
cv2.imwrite('only_crater'+'.jpg',image)