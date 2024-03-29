# import the necessary packages
import numpy as np
import argparse
import cv2
import time


from time import sleep
#from picamera import PiCamera

#camera = PiCamera()
#camera.resolution = (1024, 768)
#camera.start_preview()
# Camera warm-up time
#sleep(2)

# define the list of boundaries
boundaries = [
#BGR
	([17, 15, 100], [50, 56, 255], 'red'),
	([17, 100, 15], [80, 255, 80], 'green'),
	([103, 86, 65], [145, 133, 128], 'yellow'), 
]
#img = cv2.imread('green.png')

def checkColor():

	cap = cv2.VideoCapture(0)
	_, img = cap.read()

	# loop over the boundaries
	check = []

	for (lower, upper, color) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype="uint8")
		upper = np.array(upper, dtype="uint8")

		# find the colors within the specified boundaries and apply
		# the mask

		mask = cv2.inRange(img, lower, upper)
		output = cv2.bitwise_and(img, img, mask=mask)
		percentage = np.count_nonzero(output) * 100 / output.size
		
		# the color is dominant (considerable)
		if percentage>0:
			#print("Has {}".format(color))
			check.append([percentage, color])
		
	check.sort(key=lambda x: x[0])
	return check 

while 1:
	color = checkColor()

	if color!=[]:
		if color=='red':
			pass
			#Stop
		elif color=='yellow':
			#slow down
			pass
		elif color=='green'
			#speed up
			pass
		print(color)
	else:
		print("No red or green detected !")
	sleep(1)