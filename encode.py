import face_recognition
import os
import pickle
import cv2

known_faces = []
known_names = []

dataset_path = "dataset"

def preprocess(img):
    # Resize (helps detection)
    img = cv2.resize(img, None, fx=0.5, fy=0.5)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Improve contrast
    gray = cv2.equalizeHist(gray)

    # Convert back to RGB
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    if not os.path.isdir(person_path):
        continue

    print(f"Processing: {person}")

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        try:
            img = cv2.imread(img_path)

            if img is None:
                print(f"Cannot read {img_name}")
                continue

            found = False

            # Try multiple preprocessing + rotations
            for angle in [0, 90, 180, 270]:
                if angle != 0:
                    rotated = cv2.rotate(img, {
                        90: cv2.ROTATE_90_CLOCKWISE,
                        180: cv2.ROTATE_180,
                        270: cv2.ROTATE_90_COUNTERCLOCKWISE
                    }[angle])
                else:
                    rotated = img

                processed = preprocess(rotated)

                # Try HOG model first (fast)
                face_locations = face_recognition.face_locations(processed)

                # If not found → try CNN model (strong)
                if not face_locations:
                    face_locations = face_recognition.face_locations(processed, model="cnn")

                encodings = face_recognition.face_encodings(processed, face_locations)

                if encodings:
                    known_faces.append(encodings[0])
                    known_names.append(person)
                    found = True
                    break

            if not found:
                print(f"No face found in {img_name}")

        except Exception as e:
            print(f"Error in {img_name}: {e}")

# Save encodings
with open("encodings.pkl", "wb") as f:
    pickle.dump((known_faces, known_names), f)

print("\n✅ Encodings created successfully!")
print(f"Total faces encoded: {len(known_faces)}")