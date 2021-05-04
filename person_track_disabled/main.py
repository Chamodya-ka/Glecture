#import utils
import cv2
import numpy as numpy
#import gesturedetection as gd
import time
import os
from utils import *

cap = cv2.VideoCapture(0)

ret , img = cap.read()
height, width, channels = img.shape


while ret:
	ret , img = cap.read()
	if ret==False:
		break

	flag = False
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	coords = palm_detect(gray)
	if coords:
		flag = True
		time.sleep(1)
		ret , refreshed = cap.read()
		refreshed = refreshed[coords[1]:coords[3],coords[0]:coords[2]]
		guess,scores = detect_gesture(refreshed)
		print(guess)
		if guess!="Unknown":
			#print("key stroke initializing")
			press_key(guess)

	cv2.imshow("gray image",cv2.resize(gray,(300,300)))
	if cv2.waitKey(20) & 0xff == 27:
		break
cv2.destroyAllWindows()
cap.release()



