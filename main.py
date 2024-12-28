import cv2 as cv
import numpy as numpy

img = cv.imread('srk.jpg')
img = cv.resize(img,(500,600))
gray_img = cv.GaussianBlur(img, (7,7,),0)
cv.imshow('gray', gray_img)
cv.waitKey(0)
cv.destroyAllWindows()