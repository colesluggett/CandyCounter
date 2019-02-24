import numpy as np
import cv2 as cv

img = cv.imread("four.jpg", cv.IMREAD_COLOR)

cv.imshow("img", img)

param = cv.SimpleBlobDetector_Params()

blur = cv.blur(img,(3,3))
cv.imshow('Blur', blur)


kernel = np.ones((4,4), np.uint8)

erosion = cv.erode(blur, kernel)
kernel = np.ones((4,4), np.uint8)
dilation = cv.dilate(erosion, kernel)

cv.imshow('Erosion', erosion)
cv.imshow('Dilation',dilation)

edges = cv.Canny(dilation, 10, 300)
cv.imshow('Edge', edges)
thresh = edges.copy()

kernel = np.ones((3,3), np.uint8)
edge_dilat= cv.dilate(edges, kernel)
cv.imshow('edge dialtion', edge_dilat)

circles = cv.HoughCircles(edge_dilat, cv.HOUGH_GRADIENT, 1.2, 100)
output = img.copy() 
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
 
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv.circle(output, (x, y), r, (0, 255, 0), 4)
		cv.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
	# show the output image
	cv.imshow("output", np.hstack([img, output]))


cv.waitKey(0)
cv.destroyAllWindows()
