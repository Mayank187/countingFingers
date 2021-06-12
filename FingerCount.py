import cv2
import time
import os
import math
import HandTrackingModule as htm

wCam, hCam = 1280, 960

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

myList = [1, 2, 3, 4, 5, 0]

tipIds = [4,8,12,16,20]

detector = htm.handDetector()
prevT = 0

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw = False)
    if len(lmList) != 0 :
        fingers = []
        prevT = prevT if prevT != 0 else lmList
        if lmList[4][1] > lmList[3][1]:
            fingers.append(1)

        for id in range(1,5):
            if(lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]):
                fingers.append(1)
        cv2.putText(img, f'Count:{len(fingers)}', (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)