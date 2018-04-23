"""
Nikith AnupKumar
"""

import csv
import os
import cv2 as cv
import scipy
import matplotlib as img
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np

def average(pixel):
    return np.average(pixel)

def load():
	s = "normalized_images/crater"
	t = os.listdir(s)
	#print (t)
	#print (len(t))
	totlengc = len(t)
	leng = len(t)
	np.random.shuffle(t)
	lengc = int(leng * 70 / 100)

	#print (leng)
	#non-crater

    #image = cv.imread("TE_tile3_24_001.jpg")
	grey = np.zeros((200, 200))
	tr_d = []
	cr_val=[]


	i = 0
	for i in range(0,lengc):
		img = cv.imread("normalized_images/crater/"+t[i])
		if (i==0):
			for rownum in range(len(img)):
				for colnum in range(len(img[rownum])):
					grey[rownum][colnum] = average(img[rownum][colnum])
			tr_d = np.reshape(grey,(1,40000))
			cr_val = [1]
		else:
			for rownum in range(len(img)):
				for colnum in range(len(img[rownum])):
					grey[rownum][colnum] = average(img[rownum][colnum])
			temp = np.reshape(grey,(1,40000))
			tr_d = np.append(tr_d,temp, axis = 0)
			cr_val += [1]
	#print (tr_d,len(tr_d))
	#print (cr_val , len(cr_val))


	s1 = "normalized_images/non-crater"
	t1 = os.listdir(s1)
	#print (t)
	#print (len(t))
	totlengnc = len(t1)
	leng = len(t1)
	np.random.shuffle(t1)
	lengnc = int(leng * 70 / 100)

	#print (leng)
	#non-crater

    #image = cv.imread("TE_tile3_24_001.jpg")
	grey = np.zeros((200, 200))




	i = 0
	for i in range(0,lengnc):
		img = cv.imread("normalized_images/non-crater/"+t1[i])

		for rownum in range(len(img)):
			for colnum in range(len(img[rownum])):
				grey[rownum][colnum] = average(img[rownum][colnum])
		temp = np.reshape(grey,(1,40000))
		tr_d = np.append(tr_d,temp, axis = 0)
		cr_val += [0]
	#print (tr_d,len(tr_d))
	print ( len(cr_val))

	header = []
	with open('training_data.csv','w',newline='') as f:
		twriter = csv.writer(f)
		for y in range(1,40001):
			header +=["pixel"+str(y)]
		header += ["output"]
		twriter.writerow(header)
		l = 0
		for item in tr_d:
			twriter.writerow(item+[cr_val[l]])
			l += 1
load()
