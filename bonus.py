import cv2 as cv
import numpy as np

#reading the image as grid of pixel
img = cv.imread('color-shapes.jpg') 


#showing the image
cv.imshow('color-shapes.jpg',img)

#specifying hsu value limits for green
lower = np.array([40,150,20])
upper = np.array([75,255,255])

#converting image from bgr to hsv format, applying mask and displaying mask
image = cv.cvtColor(img,cv.COLOR_BGR2HSV)
mask = cv.inRange(image,lower,upper)

cv.imshow('mask',mask)

#holds the image display until a keyboard key is pressed
cv.waitKey(0)
