import cv2
import os
import pickle 
import face_recognition
import numpy as np
import cvzone

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

img_background=cv2.imread('Resources/background.png')

FolderModePath='Resources/Modes'
ModePathList=os.listdir(FolderModePath)
imgModeList=[]
for path in ModePathList:
    imgModeList.append(cv2.imread(os.path.join(FolderModePath,path)))

with open("EncodeFile.pkl", "rb") as file: 
    encoding_list_with_ids=pickle.load(file)

encoding_list_known,student_ids=encoding_list_with_ids
print(student_ids)

while True:
    success,img=cap.read()

    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    face_current_frame=face_recognition.face_locations(imgS)
    encode_current_frame=face_recognition.face_encodings(imgS,face_current_frame)

    img_background[162:162+480, 55:55+640]=img
    img_background[44:44+633, 808:808+414]=imgModeList[3]

    for encode_face, face_loc in zip(encode_current_frame,face_current_frame):
        matches=face_recognition.compare_faces(encoding_list_known,encode_face)
        face_dist=face_recognition.face_distance(encoding_list_known,encode_face)

        y1,x2,y2,x1=face_loc
        y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
        bbox=55+x1,162+y1, x2-x1, y2-y1
        img_background=cvzone.cornerRect(img_background, bbox,rt=0)


    match_index=np.argmin(face_dist)

    if matches[match_index]:
        # print("Known Face Detected")
        # print(student_ids[match_index])
        pass

    cv2.imshow('Background',img_background)
    if cv2.waitKey(1) & 0xFF==27:
        break