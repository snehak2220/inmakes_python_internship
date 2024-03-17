import cv2
img=cv2.imread('michel.jpg',1)
print(img)
cv2.imshow("image",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()