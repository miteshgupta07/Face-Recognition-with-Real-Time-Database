import cv2
import os

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

img_background=cv2.imread('Resources/background.png')

FolderModePath='Resources/Modes'
ModePathList=os.listdir(FolderModePath)
imgModeList=[]
for path in ModePathList:
    imgModeList.append(cv2.imread(os.path.join(FolderModePath,path)))


while True:
    success,img=cap.read()
    img_background[162:162+480, 55:55+640]=img
    img_background[44:44+633, 808:808+414]=imgModeList[3]

    cv2.imshow('Background',img_background)
    if cv2.waitKey(1) & 0xFF==27:
        break