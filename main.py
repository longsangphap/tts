from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import os

app = Flask(__name__)
audio_folder = "audio"
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)
# API để nhận văn bản và chuyển thành MP3
@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Chuyển văn bản thành giọng nói
    tts = gTTS(text, lang='vi')

    # Lưu file MP3

    mp3_filename = os.path.join(audio_folder, "output.mp3")
    tts.save(mp3_filename)

    return send_file(mp3_filename, as_attachment=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
