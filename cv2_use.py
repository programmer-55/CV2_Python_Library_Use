import cv2

#import an image
img_color = cv2.imread('butterfly.jpg', 1)
img_greyscale = cv2.imread('butterfly.jpg', 0)

#find the dimension of the image.
dimension_color = img_color.shape
print('Image Dimensions: ',dimension_color)
dimension_greyscale = img_greyscale.shape
print('Image Dimensions: ',dimension_greyscale)

#show the image.
cv2.imshow('color image', img_color)
cv2.waitKey(0)
cv2.imshow('greyscale image', img_greyscale)
cv2.waitKey(0)

#image downscaling.
down_height = 200
down_width = 400
down_points = (down_width, down_height)
resized_down = cv2.resize(img_color, down_points, interpolation = cv2.INTER_LINEAR)
dimension_down_resized = resized_down.shape
print('Down Resized Image Dimension: ',dimension_down_resized)

cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.waitKey(0)

#image upscaling.
up_height = 400
up_width = 700
up_points = (up_width,up_height)
resized_up = cv2.resize(img_color, up_points, interpolation = cv2.INTER_LINEAR)
dimension_up_resized = resized_up.shape
print('Up Resized Image Dimension: ',dimension_up_resized)

cv2.imshow('Resized Up by defining height and width', resized_up)
cv2.waitKey(0)
cv2.destroyAllWindows()

#image cropping.
cropped_img = img_color[100:200, 300:500]
dimension_cropped = cropped_img.shape
print('Cropped Image Dimension: ', dimension_cropped)

cv2.imshow('Cropped Image: ',cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#image Rotation.
height, width = img_color.shape[:2]
center = (width/2, height/2)
rotate_matrix = cv2.getRotationMatrix2D(center = center, angle=180, scale = 1)
rotated_img = cv2.warpAffine(src=img_color, M=rotate_matrix, dsize=(width,height))

cv2.imshow('Rotated image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()











