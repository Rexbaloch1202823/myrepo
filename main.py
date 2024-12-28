import cv2 as cv
import numpy as np

img = cv.imread('srk.jpg')
img = cv.resize(img,(500,500))
gray_img = cv.GaussianBlur(img, (7,7,),0)
h = np.hstack(img, gray_img)
v = np.vstack(h)
cv.imshow('gray', v)
cv.waitKey(0)
cv.destroyAllWindows()