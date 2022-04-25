import cv2 as cv
import numpy as np

image = cv.imread("robotic_arm.jpg")

#print("size:\t{}".format(image.shape)) #I reached shape datas from this code, it is (476, 910, 3)

image[400, 900] = [255,255,255] #to make white relevant pixel
#[a,b,c] is rgb color parameters
for i in range(910):
    image[200, i] = [0,255,0] # this loop draws a green line across the width of the shape 200px below the top of the shape

cv.imshow("new image", image)  

cv.waitKey(0)
cv.destroyAllWindows()