import cv2
source=""
image=cv2.imread("harry-pro.jpeg",cv2.IMREAD_UNCHANGED)

cv2.imshow("title",image)

'''percent by which image is resized'''
scale_percent=50

width=int(image.shape[1] * scale_percent /100)
height=int(image.shape[0] * scale_percent /100)

#dsize
dsize=(width,height)
out=cv2.resize(image,dsize)

cv2.imwrite('newimg.jpeg',out)

cv2.waitKey(0)


