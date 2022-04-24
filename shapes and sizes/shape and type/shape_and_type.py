import cv2
import numpy as np


image1 = cv2.imread("pic_1.jpg")
image2 = cv2.imread("pic_2.png")

image3 = cv2.imread("pic_1.jpg", 0) # to make them black and size to reduce size of images
image4 = cv2.imread("pic_2.png", 0)

print("the size of the first image (RGB) is {}".format(image1.size))
print("the type of the first image(RGB) is {}".format(image1.dtype))
print("the shape of the first image(RGB) is {} ".format(image1.shape))

print("the size of the second image (RGB) is {}".format(image2.size))
print("the type of the second image(RGB) is {}".format(image2.dtype))
print("the shape of the second image(RGB) is {} ".format(image2.shape))

print("the size of the first image is {}".format(image3.size))
print("the type of the first image is {}".format(image3.dtype))
print("the shape of the first image is {} ".format(image3.shape))

print("the size of the second image  is {}".format(image4.size))
print("the type of the second image is {}".format(image4.dtype))
print("the shape of the second image is {} ".format(image4.shape))


cv2.waitKey(0)
cv2.destroyAllWindows()