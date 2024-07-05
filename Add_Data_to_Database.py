import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(".\serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"Firebase Real Time database URL"
})


ref=db.reference('Students')

data = {
    
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)