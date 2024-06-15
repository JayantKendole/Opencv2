import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    image2 = cv2.rectangle(image, (100, 100), (200, 200), (128, 128, 128), -1)
    

    cv2.imshow('frame',image)

    if cv2.waitKey(1)== ord('q'): #Closes the windwo only when we press q
        break

cap.release()
cv2.destroyAllWindows()

