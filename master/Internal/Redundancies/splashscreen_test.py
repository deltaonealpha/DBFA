import os
import cv2 
image = cv2.imread("imagepx.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("deltaStoreManager - LOADING....... ", image)
cv2.waitKey(5000)
os.startfile(r'C:\Users\balaj\OneDrive\Desktop\dsmsapl-master\maintester1.py')
cv2.destroyAllWindows()
