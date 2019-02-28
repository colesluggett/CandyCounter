import numpy as np
import cv2 as cv

img = cv.imread("one.jpg", cv.IMREAD_COLOR)

cv.imshow("img", img)

param = cv.SimpleBlobDetector_Params()

blur = cv.blur(img,(3,3))
#cv.imshow('Blur', blur)


kernel = np.ones((4,4), np.uint8)

erosion = cv.erode(blur, kernel)
kernel = np.ones((4,4), np.uint8)
dilation = cv.dilate(erosion, kernel)

#cv.imshow('Erosion', erosion)
#cv.imshow('Dilation',dilation)

edges = cv.Canny(dilation, 10, 300)
#cv.imshow('Edge', edges)
thresh = edges.copy()

kernel = np.ones((3,3), np.uint8)
edge_dilat= cv.dilate(edges, kernel)
#cv.imshow('edge dialtion', edge_dilat)

circles = cv.HoughCircles(edge_dilat,cv.HOUGH_GRADIENT,1,20,param1=50,param2=25,minRadius=10,maxRadius=40)

circles = np.uint16(np.around(circles))
listOfCircleImages = [] 
for i in circles[0,:]:
    currentImg = np.zeros((img.shape[0],img.shape[1]), np.uint8) 
    cv.circle(currentImg,(i[0],i[1]),i[2],(255,255,255), -1) 
    cv.circle(edge_dilat,(i[0],i[1]),i[2],(255,255,255), -1) 
    listOfCircleImages.append(currentImg)
    
for img in listOfCircleImages:
    rgb_data = cv.mean(img, mask=img)



font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Yellow Red Blue Green Brown Orange', (0,0), font, 1, (200,255,255), 2, cv.LINE_AA)

cv.imshow('Detected Circles',edge_dilat)

'''
M&M's  rgb color
Green 49 172 215
Yellow 255 242 0
Orange 242 111 34
Brown 96 58 52
Red 177 18 36
Blue 47 159 215
'''

cv.waitKey(0)
cv.destroyAllWindows()
