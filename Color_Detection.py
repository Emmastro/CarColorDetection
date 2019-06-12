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
# BGR
	([17, 15, 100], [50, 56, 255], 'red'),  # Red
	([17, 100, 15], [80, 255, 80], 'green')  # green
]
#img = cv2.imread('green.png')
cap = cv2.VideoCapture(0)
_, img = cap.read()

print("Image read ")

def checkColor():

	# loop over the boundaries
	check = []
	print("Cheking Colors ")
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
		print('Check {}'.format(color))
		
	check.sort(key=lambda x: x[0])
	return check 

color = checkColor()

if color!=[]:
	print(color)
	print(color[-1][1])
else:
	print("No red or green detected !")