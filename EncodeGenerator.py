import cv2
import face_recognition
import pickle
import os 

folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])


def find_encodings(imageList):
    encoding_list_known=[]
    for img in imageList:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encodings=face_recognition.face_encodings(img)[0]
        encoding_list_known.append(encodings)
    
    return encoding_list_known

print("Encoding Started......")

encoding_list_known=find_encodings(imgList)

print("Encoding Completed......")

encoding_list_with_ids=[encoding_list_known,studentIds]

with open("EncodeFile.pkl", "wb") as file: 
    pickle.dump(encoding_list_with_ids, file)

print("File Saved......")