import cv2 as cv

#reading the image as grid of pixel
img = cv.imread('color-shapes.jpg') 


#showing the image
cv.imshow('color-shapes.jpg',img)

#converting the image to grayscale and showing that grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#detecting edges
canny = cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)

#finding contours using method which returns contours and heirarchies
contours, heirarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')


#holds the image display until a keyboard key is pressed
cv.waitKey(0)
