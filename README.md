
# 🚨 Real-Time Intruder Detection and Notification System

A smart security system using **Computer Vision,** **face recognition** and **real-time notifications** to detect unknown intruders and alert the homeowner via **SMS** and a loud **audio beep**.

---

## 📌 Overview

In today's world, ensuring secure residential spaces is crucial. Traditional systems like fiber sensors or accelerometers are often unreliable, expensive, and environmentally sensitive. Our system addresses these limitations by using **machine learning**, **face recognition**, and **IoT-enabled communication** to detect intruders in real time and immediately notify the owner.

This system captures faces via webcam, checks if they are known, and if not:
- Triggers a **beep alert**.
- Sends an **SMS notification** to the homeowner.

---

## 🧰 Technologies Used

| Tool/Library     | Purpose                                |
|------------------|----------------------------------------|
| Python           | Core programming language              |
| OpenCV           | Real-time video processing             |
| face_recognition | Face detection and encoding            |
| Twilio API       | Sending SMS alerts                     |
| winsound         | Audio alerts (Windows only)            |
| Webcam + Speaker | Real-time monitoring and beeping       |

---

## 📁 Project Structure

```
📦 Real-Time-Intruder-Detection/
 ┣ 📂 known_faces/         # Store known face images here
 ┣ 📜 intruder_alert.py    # Main Python script
 ┗ 📜 README.md            # This file
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Real-Time-Intruder-Detection.git
cd Real-Time-Intruder-Detection
```

### 2. Install dependencies

```bash
pip install opencv-python face_recognition twilio
```

### 3. Add known faces

Place clear frontal face images (JPG or PNG) of known people in the `known_faces/` folder.  
The file names (excluding the extension) will be used as the person's name.

```
known_faces/
├── Alice.jpg
├── Bob.png
```

### 4. Update credentials

In `intruder_alert.py`, update these values:

```python
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_phone_number = '+1234567890'
your_phone_number = '+0987654321'
known_faces_dir = "known_faces"
```

### 5. Run the system

```bash
python intruder_alert.py
```

Press **`q`** to quit the video stream.

---

## ⚙️ How It Works

1. Loads all known faces from the `known_faces` folder and encodes them.
2. Captures real-time video using your webcam.
3. For each detected face:
   - If it matches a known encoding, the name is displayed.
   - If it's **unknown**, a **beep alert** is played and an **SMS is sent** via Twilio.

---

## 🔐 Benefits

- No need for traditional sensors (e.g., accelerometers)
- Resilient to environmental factors like temperature
- Real-time alert system
- Works with basic hardware (camera + speaker)

---

## 💡 Future Enhancements

- Add GUI for registering new faces
- Email and mobile app notifications
- Deploy on Raspberry Pi for portability
- Add face detection logs and timestamps
- Multi-camera support
- Face dataset sync via cloud

---

## 🙌 Credits

Built with:
- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [Twilio API](https://www.twilio.com/)
- [Python](https://www.python.org/)

---

## 🛑 Disclaimer

This project is for educational and ethical use only. Do not use for unauthorized surveillance.

---

## 📞 Contact

For queries, improvements, or collaborations, feel free to reach out via GitHub or [LinkedIn](https://www.linkedin.com/in/pnaveenchary/)
