import cv2

import numpy as np

image = cv2.imread("pic_1.jpg", 0) # if zero added at the end, the image will be black and white. Thus in this code, relevant image will be black and white
cv2.imshow("title", image)
# cv2.imwrite("new_name_of_the_image") to save as a new image
#print(image) give us matris form of image also
cv2.waitKey(0)
cv2.destroyAllWindows()
