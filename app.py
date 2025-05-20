from flask import Flask, render_template, Response, request, redirect
import cv2
from deepface import DeepFace

app = Flask(__name__)

# Cámara
camera = cv2.VideoCapture(0)

# Emoción que se debe imitar (por defecto: felicidad)
emocion_actual = "happy"

# Emociones posibles en DeepFace (por si deseas validar)
emociones_validas = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

def gen_frames():
    global emocion_actual
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            try:
                # Analizar emoción
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                emotion = result[0]['dominant_emotion']

                if emotion == emocion_actual:
                    mensaje = "Muy bien!"
                    color = (0, 255, 0)
                else:
                    mensaje = f"Emocion detectada: {emotion}"
                    color = (0, 0, 255)

                cv2.putText(frame, mensaje, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            except Exception as e:
                cv2.putText(frame, "Analizando...", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Codificar y enviar el frame
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template("index.html", emocion_actual=emocion_actual)



@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/set_emotion', methods=['POST'])
def set_emotion():
    global emocion_actual
    emotion = request.form.get('emotion', 'happy')
    if emotion in emociones_validas:
        emocion_actual = emotion
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
