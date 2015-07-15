import numpy as np
import cv2 as cv
#reads image as greyscale
img = cv.imread("image.jpg",0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
