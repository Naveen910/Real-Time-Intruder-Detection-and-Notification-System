import cv2
import face_recognition
import os
import winsound
import twilio
from twilio.rest import Client

# Twilio credentials (Removed for security purposes)
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_phone_number = '+19145024040'
your_phone_number = '+918919885377'

# Load known face encodings and their corresponding names
known_face_encodings = []
known_face_names = []

# Load known faces and encode them
known_faces_dir = "D:/Desktop/MAJOR PROJECT/Faces"  # Replace with your directory containing known faces

for filename in os.listdir(known_faces_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(known_faces_dir, filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(filename.split('.')[0])

# Initialize Twilio client
# client = Client(account_sid, auth_token)  # Removed for security purposes

# Open the default camera (0) or a specific camera (1, 2, etc.)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find face locations and encodings in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Compare the detected face with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match is found, use the name of the known face
        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]

        # If the face is unknown, play a beep sound and send SMS
        if name == "Unknown":
            print("Intruder Detected!")
            winsound.Beep(1000, 1500)  # Beep with frequency 1000Hz for 1500 milliseconds

            # Send SMS using Twilio
            # message = client.messages.create(
            #     body='Intruder detected!',
            #     from_='+19145024040',
            #     to='+918919885377'
            # )

        # Display the name of the recognized face
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
