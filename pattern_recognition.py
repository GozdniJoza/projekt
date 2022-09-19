from tkinter.messagebox import NO
import cv2 as cv
import numpy as np

#img1 = cv.imread('img1.png')
img1 = cv.VideoCapture(0)
img2 = cv.imread('img2.png')



orb = cv.ORB_create(nfeatures=1000)

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)


#Najde ustrezne matche
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])


img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2, good,None,flags=2)
cv.imshow('img3', img3)
cv.waitKey(0)

