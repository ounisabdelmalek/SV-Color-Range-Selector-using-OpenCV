import cv2
import numpy as np

def nothing(s):
    return None

img = cv2.imread("your image")
img = cv2.resize(img,(512,512))
cv2.namedWindow('config')
cv2.createTrackbar("LH", 'config', 0, 179, nothing)   # OpenCV hue max = 179
cv2.createTrackbar("LS", 'config', 0, 255, nothing)
cv2.createTrackbar("LV", 'config', 0, 255, nothing)
cv2.createTrackbar("UH", 'config', 179, 179, nothing)
cv2.createTrackbar("US", 'config', 255, 255, nothing)
cv2.createTrackbar("UV", 'config', 255, 255, nothing)
while(True):
    hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

    l_h = cv2.getTrackbarPos('LH','config')
    l_s = cv2.getTrackbarPos('LS','config')
    l_v = cv2.getTrackbarPos('LV','config')

    u_h = cv2.getTrackbarPos('UH','config')
    u_s = cv2.getTrackbarPos('US','config')
    u_v = cv2.getTrackbarPos('UV','config')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv,l_b,u_b) # make images in this range l_b,u_b white and the others black

    res = cv2.bitwise_and(hsv,hsv,mask=mask)

    cv2.imshow("res",res)
    cv2.imshow('originale',img)
    cv2.imshow("mask",mask)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
