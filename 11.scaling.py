import cv2 as cv

img = cv.imread('Test1.jpg')

cv.imshow('Bird',img)

def rescaleFrame(frame, scale=0.3):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)


resized_img = rescaleFrame(img)

cv.imshow('Image',resized_img)
   

cv.waitKey(0)