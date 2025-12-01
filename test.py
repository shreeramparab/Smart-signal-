import cv2
import numpy as np
import time
from flask import Flask, Response, jsonify, render_template

app = Flask(__name__)

# Load Haar Cascade XML
cascade = cv2.CascadeClassifier(r"C:\Users\devgu\Downloads\haarcascade_frontalface_alt2.xml")

cap = cv2.VideoCapture(0)
color = 'green'
last_switch = time.time()

def detect_object_and_draw(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return len(objects) > 0, frame

def gen_frames():
    global color, last_switch
    while True:
        success, frame = cap.read()
        if not success:
            break

        object_detected, frame_with_boxes = detect_object_and_draw(frame)

        # Signal logic remains the same
        if object_detected:
            color = 'red'
        else:
            if time.time() - last_switch > 2:
                color = 'red' if color == 'green' else 'green'
                last_switch = time.time()

        ret, buffer = cv2.imencode('.jpg', frame_with_boxes)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/signal')
def signal_state():
    return jsonify({"color": color})

if __name__ == "__main__":
    app.run(debug=True)