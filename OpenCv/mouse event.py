import cv2

def drawCircle(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),100,(255,0,0),-1)
image=cv2.imread("michel.jpg",1)
cv2.namedWindow("image")
cv2.setMouseCallback("image",drawCircle)
while (1):
    cv2.imshow('image',image)
    cv2.waitKey(0)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()