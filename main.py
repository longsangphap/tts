from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import io

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Server is running"


@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Chuyển văn bản thành giọng nói và lưu vào bộ nhớ (chưa lưu vào tệp)
    tts = gTTS(text, lang='vi')

    # Tạo một buffer trong bộ nhớ để lưu tệp MP3
    mp3_file = io.BytesIO()
    tts.save(mp3_file)
    mp3_file.seek(0)  # Đặt lại con trỏ tệp về đầu

    # Trả về file MP3 dưới dạng đính kèm
    return send_file(mp3_file, mimetype='audio/mpeg', as_attachment=True, attachment_filename='output.mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
