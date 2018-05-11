
# import the necessary packages


import argparse
import time
import cv2
import imutils
 
 
 
 
def sliding_window(img, stepSize, windowSize):
	for y in xrange(0, img.shape[0], stepSize):
		for x in xrange(0, img.shape[1], stepSize):
			yield (x, y, img[y:y + windowSize[1], x:x + windowSize[0]])
			
			
			
			
			
			

def pyramid(img, scale=1.5, minSize=(30, 30)):

	#yield image
 

	while True:
		w = int(img.shape[1] / scale)
		img = imutils.resize(img, width=w)
		if img.shape[0] < minSize[1] or img.shape[1] < minSize[0]:
			break
		yield img

def crop(x,y,w,h,image,name):
	#img = cv2.imread("tile3_24.png")
	crop_img = image[x:x+w, y:y+h]
	cv2.imwrite('alldata/'+name+'.jpg',crop_img)
	return 





ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and define the window width and height
image = cv2.imread(args["image"])
(winW, winH) = (101, 101)

# loop over the image pyramid
reno=0
for resized in pyramid(image, scale=1.5):
	reno+=1
	wino=0
	
	
	for (x, y, window) in sliding_window(resized, stepSize=32, windowSize=(winW, winH)):
		# if the window does not meet our desired window size, ignore it
		if window.shape[0] != winH or window.shape[1] != winW:
			continue
		wino+=1
		#print(reno)
		#print("---")
		#print(wino)
		#print("\t")
		clone = resized.copy()
		clone1 = resized.copy()
		cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 255), 3)
		name ="all_data"+str(reno)+"_"+str(wino)
		crop(x,y,winW,winH,clone1,name)
		cv2.imshow("Window", clone)
		cv2.waitKey(1)
		time.sleep(0.025)
	print("\n")