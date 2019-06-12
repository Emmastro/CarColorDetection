# import the necessary packages
import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
#args = vars(ap.parse_args())
 
# load the image
#image = cv2.imread('yellow.jpg')#args["image"])


# define the list of boundaries
boundaries = [
#BGR
	([17, 15, 100], [50, 56, 255]), #Red
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128]),
	([17, 100, 15], [80, 255, 80])#green
]
img = cv2.imread('color_detection.jpg')
cap = cv2.VideoCapture(0)
#_, img = cap.read()

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask

	mask = cv2.inRange(img, lower, upper)
	output = cv2.bitwise_and(img, img, mask = mask)
	print(np.count_nonzero(output)*100/output.size)
	# show the images
	#print(np.hstack([output]).tolist())
	cv2.imshow("images", np.hstack([output]))
	cv2.waitKey(0)