import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

cv2.line(img,(0,290),(512,290),(255,0,0),5)

cv2.rectangle(img,(220,200),(300,300),(0,0,255),-1)

cv2.ellipse(img,(256,256),(100,50),0,0,180,120,-1)  # half ellipse to make it full change 0,0,180 to 0,-180,180

cv2.circle(img,(447,63), 63, (0,128,230), -1)

cv2.imshow('Shapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
