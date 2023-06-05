from flask import Flask, render_template, request
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

loaded_model = tf.keras.models.load_model("driver_effecient_net_b0.h5")

labels=['Safe driving','Texting - right','Talking on the phone - right', 'Texting - left',
             'Talking on the phone - left', 'Operating the radio', 'Drinking', 'Reaching behind', 'Hair and makeup', 'Talking to passenger']



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['video']
    video_path = 'static/videos/' + file.filename
    file.save(video_path)

    return render_template('video.html', video_path=video_path)

@app.route('/video_feed')
def video_feed():
    video_path = request.args.get('video_path')

    cap = cv2.VideoCapture(video_path)

    def generate_frames():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Process the frame here (e.g., convert to grayscale)
            # processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            img= np.copy(frame)
            img=cv2.resize(img,(460,480))
            pred_prob = loaded_model.predict(tf.expand_dims(img, axis=0),verbose=0)
            pred_class = labels[pred_prob.argmax()] # find the predicted class
            cv2.putText(frame, pred_class, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Convert the processed frame to JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # Yield the frame in the response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return app.response_class(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
