import cv2
import face_recognition
import pickle
import os 

FolderPath='Images'
ModePathList=os.listdir(FolderPath)
imgList=[]
for path in ModePathList:
    imgList.append(cv2.imread(os.path.join(FolderPath,path)))
