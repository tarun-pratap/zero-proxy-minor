import sys
import face_recognition
import cv2
import numpy as np
import json

# Load images and encode faces
obama_image = face_recognition.load_image_file("9921103118.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
biden_image = face_recognition.load_image_file("9921103163.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
pratham_image = face_recognition.load_image_file("9921103103.jpg")
pratham_face_encoding = face_recognition.face_encodings(pratham_image)[0]
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    pratham_face_encoding
]
known_face_names = [
    "9921103118",
    "9921103163",
    "9921103103"
]

# Initialize video capture
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        face_names.append(name)
    # Construct JSON object
    output_json = json.dumps({"face_name": face_names})
    print(output_json, flush=True)  # Print JSON object to stdout
    if(len(face_names)>0):
        break

