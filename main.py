from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Server is running"

audio_folder = "audio";
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Chuyển văn bản thành giọng nói và lưu vào bộ nhớ (chưa lưu vào tệp)
    tts = gTTS(text, lang='vi')

    # Tạo một buffer trong bộ nhớ để lưu tệp MP3
    mp3_file = os.path.join(audio_folder, "output.mp3")
    tts.save(mp3_file)

    # Trả về file MP3 dưới dạng đính kèm
    return send_file(mp3_file, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
