# 🙎‍♂️Face Recognition System with Real-Time Database

## 📋 Overview

This project is a Face Recognition System that generates face encodings for stored data and uses these encodings to recognize new faces. When a new face is recognized, the data is added to a real-time database using Firebase.

## ✨ Features

- **🔢 Face Encoding Generation:** Generates unique encodings for faces stored in the database.
- **🕵️ Real-Time Face Recognition:** Recognizes new faces using the generated encodings.
- **🔄 Real-Time Database Integration:** Adds recognized face data to Firebase in real-time.

## 🛠️ Technologies Used

- Python
- OpenCV
- dlib
- Firebase

## 🚀 Installation

To get started with the project, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/face-recognition-system.git
    cd face-recognition-system
    ```

2. **Create and Activate Virtual Environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup Firebase:**
    - Create a Firebase project in the [Firebase Console](https://console.firebase.google.com/).
    - Add a real-time database to your project.
    - Download the `serviceAccountKey.json` file from Firebase and place it in your project directory.

## 📘 Usage

1. **Generate Face Encodings:**
    - Run the script to generate face encodings for stored data.
    ```bash
    python EncodingGenerator.py
    ```

2. **Recognize New Faces:**
    - Run the script to start recognizing new faces and adding data to Firebase in real-time.
    ```bash
    python main.py
    ```

## ⚙️ Configuration

Make sure to configure your Firebase settings in the `firebase_config.json` file. Here is a template:

```json
{
  "apiKey": "YOUR_API_KEY",
  "authDomain": "YOUR_PROJECT_ID.firebaseapp.com",
  "databaseURL": "https://YOUR_PROJECT_ID.firebaseio.com",
  "storageBucket": "YOUR_PROJECT_ID.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}
```

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## 📄License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/miteshgupta07/Face-Recognition-with-Real-Time-Database/blob/main/LICENSE) file for details.

## 📧Contact
If you have any questions or feedback, feel free to reach out to me at miteshgupta2711@gmail.com.
