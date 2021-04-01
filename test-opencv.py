#이미지에 사각형 그리기
import cv2

image_path = './image/Ragdoll/ragdoll1.jpg'
image = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)

image2= cv2.rectangle(image,(10,10),(20,20),(255,255,255),2)



cv2.imshow("original",image)
cv2.imshow("rectangle",image2)

cv2.waitKey(0)
