import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import cv2
import face_recognition
import pickle
import pandas as pd
from datetime import datetime

TOLERANCE = 0.45  
FRAME_RESIZE = 0.25  

with open("encodings.pkl", "rb") as f:
    known_encodings, known_names = pickle.load(f)

video = cv2.VideoCapture(0)

marked_names = []

date_today = datetime.now().strftime("%Y-%m-%d")
file_name = f"attendance_{date_today}.xlsx"

try:
    df = pd.read_excel(file_name)
except:
    df = pd.DataFrame(columns=["Name", "Time"])

print("Press 'q' to stop attendance...")

while True:
    ret, frame = video.read()

    if not ret:
        print("Camera not working")
        break

    small_frame = cv2.resize(frame, (0, 0), fx=FRAME_RESIZE, fy=FRAME_RESIZE)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):

        face_distances = face_recognition.face_distance(known_encodings, face_encoding)

        name = "Unknown"

        if len(face_distances) > 0:
            best_match_index = face_distances.argmin()
            best_distance = face_distances[best_match_index]

            print(f"Distance: {best_distance:.3f}")

            if best_distance < TOLERANCE:
                name = known_names[best_match_index]

        if name != "Unknown" and name not in marked_names:
            now = datetime.now()
            time_string = now.strftime("%H:%M:%S")

            new_entry = pd.DataFrame([[name, time_string]], columns=["Name", "Time"])
            df = pd.concat([df, new_entry], ignore_index=True)

            marked_names.append(name)
            print(f"✅ {name} marked present")

        top, right, bottom, left = face_location
        top *= int(1/FRAME_RESIZE)
        right *= int(1/FRAME_RESIZE)
        bottom *= int(1/FRAME_RESIZE)
        left *= int(1/FRAME_RESIZE)

        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)

        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        label = f"{name}"
        cv2.putText(frame, label, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        
    cv2.imshow("Face Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

df.to_excel(file_name, index=False)

video.release()
cv2.destroyAllWindows()

print("📊 Attendance saved successfully!")
