import cv2
import os
import pickle 
import face_recognition
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage,db
from datetime import datetime

cred = credentials.Certificate(".\serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"Firebase Real Time database URL",
    "storageBucket":"Firebase Storage Bucket URL"
})

bucket=storage.bucket()

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
# print(student_ids)

modeType=0
counter=0
id=-1
img_student=[]

while True:
    success,img=cap.read()

    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    face_current_frame=face_recognition.face_locations(imgS)
    encode_current_frame=face_recognition.face_encodings(imgS,face_current_frame)

    img_background[162:162+480, 55:55+640]=img
    img_background[44:44+633, 808:808+414]=imgModeList[modeType]

    if face_current_frame:
        for encode_face, face_loc in zip(encode_current_frame,face_current_frame):
            matches=face_recognition.compare_faces(encoding_list_known,encode_face)
            face_dist=face_recognition.face_distance(encoding_list_known,encode_face)


            match_index=np.argmin(face_dist)

            if matches[match_index]:
                y1,x2,y2,x1=face_loc
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                bbox=55+x1,162+y1, x2-x1, y2-y1
                img_background=cvzone.cornerRect(img_background, bbox,rt=0)
                # print("Known Face Detected")
                # print(student_ids[match_index])
                id=student_ids[match_index]
                if counter==0:
                    cvzone.putTextRect(img_background, "Loading", (275, 400))
                    cv2.imshow('Face Recognition',img_background)
                    cv2.waitKey(1)
                    counter=1
                    modeType=1
        
        if counter!=0:
            if counter==1:
                student_info=db.reference(f'Students/{id}').get()
                # print(student_info)

                blob=bucket.get_blob(f'Images/{id}.png')
                array=np.frombuffer(blob.download_as_string(),np.uint8)
                img_student=cv2.imdecode(array,cv2.COLOR_BGRA2BGR)

                datetime_obj=datetime.strptime(student_info['last_attendance_time'],"%Y-%m-%d %H:%M:%S")
                time_elapsed=(datetime.now()-datetime_obj).total_seconds()
                # print(time_elapsed)

                if time_elapsed>30:
                    ref=db.reference(f'Students/{id}')
                    student_info['total_attendance']+=1
                    ref.child('total_attendance').set(student_info['total_attendance'])
                    ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType=3
                    counter=0
                    img_background[44:44+633,808:808+414]=imgModeList[modeType]
                    
            if modeType!=3:
                if 10<counter<20:
                    modeType=2
                img_background[44:44+633,808:808+414]=imgModeList[modeType]

                if counter<=10:
                    cv2.putText(img_background, str(student_info['total_attendance']), (861, 125), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                    cv2.putText(img_background, str(student_info['major']), (1006, 550), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(img_background, str(id), (1006, 493), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(img_background, str(student_info['standing']), (910, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(img_background, str(student_info['year']), (1025, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(img_background, str(student_info['starting_year']), (1125, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    
                    
                    (w,h),_=cv2.getTextSize(student_info['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset=(414-w)//2
                    cv2.putText(img_background, str(student_info['name']), (808+offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

                    img_background[175:175+216,909:909+216]=img_student
                counter+=1

                if counter>=20:
                    counter=0
                    modeType=0
                    student_info=[]
                    img_student=[]
                    img_background[44:44+633,808:808+414]=imgModeList[modeType]

    else:
        modeType=0
        counter=0
    

    cv2.imshow('Face Recognition',img_background)
    if cv2.waitKey(1) & 0xFF==27:
        break