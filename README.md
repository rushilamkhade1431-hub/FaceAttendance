# Face Attendance System

This project is a simple face recognition based attendance system developed using Python.

The system uses a webcam to recognize registered members and automatically records their attendance along with the time. The attendance is saved in an Excel file, and a separate file is created for each date.

## About the Project

Taking attendance manually can take time, especially when there are many members. This project was made to automate the basic attendance process using face recognition.

The system first creates face encodings from the images stored in the dataset. These encodings are then used when the webcam is running to compare the detected face with the registered faces.

When a registered person is recognized, their name and the current time are added to the attendance file.

## How the System Works

The project mainly works in two steps:

### 1. Creating Face Encodings

The `encode.py` file reads the images from the `dataset` folder.

The dataset is arranged using separate folders for different people.

Example:

    dataset/
    ├── Person_1/
    ├── Person_2/
    ├── Person_3/
    └── Person_4/

The program processes the images and generates face encodings. These encodings are stored in:

    encodings.pkl

### 2. Taking Attendance

The `attendance.py` file starts the webcam and detects faces from the video.

For every detected face, the system compares its encoding with the stored encodings. If a suitable match is found, the person's name is identified.

The system then records:

- Name
- Attendance time

The attendance is saved in an Excel file with the current date.

Example:

    attendance_2026-09-13.xlsx

A person is only marked once during a single run of the attendance system.

## Features

- Real-time face recognition using a webcam
- Automatic attendance marking
- Date-wise attendance files
- Attendance time recording
- Avoids marking the same person multiple times during one session
- Unknown faces are not added to the attendance
- Face image preprocessing before recognition
- Uses a smaller frame size to improve processing speed

## Technologies Used

- Python
- OpenCV
- face-recognition
- Pandas
- OpenPyXL
- Pickle

## Project Files

    FaceAttendance/
    │
    ├── attendance.py
    ├── encode.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

The face dataset and generated face encodings are not included in this repository.

## Requirements

Python is required to run this project.

The required Python packages are listed in:

    requirements.txt

Install them using:

    pip install -r requirements.txt

## Setting Up the Dataset

Create a folder named:

    dataset

Inside it, create a separate folder for each registered person.

For example:

    dataset/
    ├── Rahul/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── image3.jpg
    │
    ├── Person2/
    │   ├── image1.jpg
    │   └── image2.jpg

Use face images that you have permission to use.

## Running the Project

### Step 1: Install the requirements

Open the terminal inside the project folder and run:

    pip install -r requirements.txt

### Step 2: Add the dataset

Add the authorized face images inside the `dataset` folder.

### Step 3: Generate the encodings

Run:

    python encode.py

This creates:

    encodings.pkl

### Step 4: Start the attendance system

Run:

    python attendance.py

The webcam will start and the system will begin recognizing registered faces.

Press:

    q

to stop the attendance system.

## Attendance Output

After running the system, an Excel file is created using the current date.

For example:

    attendance_2026-09-13.xlsx

The file contains the name of the recognized person and the time at which they were marked present.

## Privacy

This project uses face recognition, so the face images and generated face encodings should be handled carefully.

The original dataset, `encodings.pkl`, attendance records, and other personal data are not included in this public repository.

If you use this project with other people, use their face images only with proper permission.

## Limitations

The accuracy of face recognition can depend on factors such as lighting, camera quality, image quality, and the angle of the face.

The system also requires a working webcam for real-time attendance.

## Future Improvements

Some improvements that can be added in the future include:

- Adding a graphical user interface
- Adding an option to register new members from the application
- Improving recognition under different lighting conditions
- Adding an attendance dashboard
- Adding support for multiple cameras
- Adding an option to export attendance reports

## Author

Developed as a computer vision project using Python and face recognition.
