import cv2 as cv
import numpy as np

origImg = cv.imread("candyBigSmallerTiny.jpg", cv.IMREAD_COLOR)

#function that brightens picture
def brighten(img, value = 70):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)
    
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    
    final_hsv = cv.merge((h, s, v))
    img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
    return img

#brightens, blues, and detects edges of picture
origImg = brighten(origImg)
blur = cv.blur(origImg, (5, 5), 0)
kernel = np.ones((5, 5), np.uint8)
edge = cv.Canny(blur, 5, 150)

circles = cv.HoughCircles(edge, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=15, minRadius=10, maxRadius=20)
circles = np.uint16(np.around(circles))
arrayOfCircles = []
count = 0
blue = 0
green = 0
yellow = 0
orange = 0
brown = 0
red = 0
undetermined = 0

for i in circles[0, :]:
    currentImg = np.zeros((origImg.shape[0], origImg.shape[1]), np.uint8)
    cv.circle(currentImg,(i[0], i[1]), i[2]-5, (255, 255, 255), -1)
    arrayOfCircles.append(currentImg)

#for loop that checks the colors of each circle and then draws a new colored circle on the origImg
for img in arrayOfCircles:
    rgb = cv.mean(origImg, mask = img)
    count += 1
    current = circles[0,count-1]
    
    
    #blue
    if(int(rgb[0]) in range(215, 256) and int(rgb[1]) in range(155, 239) and int(rgb[2]) in range(0, 47)):
        blue += 1
        cv.circle(origImg, (current[0], current[1]), current[2], (215, 159,47), -1)
    #green
    elif(int(rgb[0]) in range(75, 200) and int(rgb[1]) in range(98, 256) and int(rgb[2]) in range(0, 50)):
        green += 1
        cv.circle(origImg, (current[0], current[1]), current[2], (85, 172, 49), -1)
    #red
    elif(int(rgb[0]) in range(90, 170) and int(rgb[1]) in range(75, 140) and int(rgb[2]) in range(204, 256)):
        red += 1
        cv.circle(origImg, (current[0],current[1]), current[2],(0, 0, 255), -1)
    #yellow
    elif(int(rgb[0]) in range(0, 70) and int(rgb[1]) in range(220, 256) and int(rgb[2]) in range(245, 256)):
        yellow += 1
        cv.circle(origImg,(current[0], current[1]),int(current[2]),(0,255,255),-1)
    #orange
    elif(int(rgb[0]) in range(32, 120) and int(rgb[1]) in range(98, 160) and int(rgb[2]) in range(245, 256)):
        orange += 1
        cv.circle(origImg, (current[0], current[1]), current[2], (34, 111, 242), -1)
    #brown
    elif(int(rgb[0]) in range(100, 215) and int(rgb[1]) in range(94, 181) and int(rgb[2]) in range(105, 161)):
        brown += 1
        cv.circle(origImg, (current[0], current[1]), current[2], (52, 58, 96), -1)
    #if it can't find a matching color, send to undetermined
    else:
        undetermined += 1

#prints out values for each color of candy

font = cv.FONT_HERSHEY_SIMPLEX


cv.putText(origImg,("Blue: " + str(blue)), (10, 30), font, 1, (210, 255, 255), 2, cv.LINE_AA)
cv.putText(origImg,("Green: " + str(green)), (10, 65), font, 1,(210,255,255),2,cv.LINE_AA)
cv.putText(origImg,("Red: " + str(red)), (10, 100), font, 1, (210, 255, 255), 2, cv.LINE_AA)
cv.putText(origImg,("Yellow: " + str(yellow)), (10, 135), font, 1, (210, 255, 255), 2, cv.LINE_AA)
cv.putText(origImg,("Orange: " + str(orange)), (10, 170), font, 1, (210, 255, 255), 2, cv.LINE_AA)
cv.putText(origImg,("Brown: " + str(brown)), (10, 205), font, 1, (210, 255, 255), 2, cv.LINE_AA)

cv.imshow("img", origImg)

cv.waitKey(0)
cv.destroyAllWindows()

