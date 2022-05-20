import cv2 as cv
import numpy as np

image = cv.imread("image.jpg")

#you can use paint to reach coordinate of the image
cv.rectangle(image, (127, 450), (343, 130), [0,0,255], 3) #x, y be carefull
#the first arg. is lower left corner, the second arg. is upper right corner, 
# the third one is what the color of the frame will be, and the last one is thickness of the frame


cv.imshow("I think he is a neandertal", image)


cv.waitKey(0)
cv.destroyAllWindows()