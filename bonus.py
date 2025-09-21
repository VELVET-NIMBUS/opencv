import cv2 as cv
import numpy as np

#reading the image as grid of pixel
img = cv.imread('color-shapes.jpg') 


#specifying hsu value limits for green
lower = np.array([40,150,20])
upper = np.array([75,255,255])

#converting image from bgr to hsv format and applying mask
image = cv.cvtColor(img,cv.COLOR_BGR2HSV)
mask = cv.inRange(image,lower,upper)

#Applying Gaussian blur (I don't know man to reduce noise maybe)
blurred = cv.GaussianBlur(mask,(5,5),0)

#Using canny for edge detection and showing image
canny = cv.Canny(blurred,125,175)
cv.imshow('Canny',canny)

#defining variables to count number of triangles and squares
trig =0
square =0

#identifying shapes
contours,hierarchy = cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
for i, contour in enumerate(contours):

    epsilon = 0.02*cv.arcLength(contour,True)
    approx = cv.approxPolyDP(contour,epsilon,True)



    if len(approx)==3:
        (x,y,w,h)= cv.boundingRect(approx)
        cv.drawContours(img,[approx],-1,(255,0,0),2)
        cv.putText(img,"Triangle",(x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
        trig +=1
    elif (len(approx)==4):
        (x,y,w,h) = cv.boundingRect(approx)
        aspect_ratio = w/float(h)

        if 0.95<= aspect_ratio <=1.05:
            cv.drawContours(img,[approx],-1,(255,0,0),2)
            cv.putText(img,"Square",(x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
            square +=1
    else:
        continue



#Putting the text
cv.putText(img,'Triangles:'+str(trig),(0,30),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
cv.putText(img,'Squares:'+str(square),(0,80),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

#showing the image
cv.imshow('color-shapes.jpg',img)


#holds the image display until a keyboard key is pressed
cv.waitKey(0)
