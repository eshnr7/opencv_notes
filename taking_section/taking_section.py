import cv2
import numpy as np

image = cv2.imread("solar_sys.jpg")

#print("size: {}".format(image.shape))  #640,1280

section = image[305:365,425:485] #there is Mars photo in this section
#there is a link between below and above code. *image[295:355,420:480,2] = 120
section[ :, :, 2] = 120 #until 255 # to make red, if 0 is written in relevant place, so it will be blue.
# it will be used more than one, so these will be a combination of color
cv2.imshow("Solay System", image)
cv2.imshow("Mars", section)

cv2.waitKey(0)
cv2.destroyAllWindows()