import os
from flask import Flask, request, send_file, jsonify

app = Flask(__name__)


PORT = int(os.environ.get("APP_PORT", 8000))
STORAGE_DIR = "/app/storage"

os.makedirs(STORAGE_DIR, exist_ok=True)

@app.route('/')
def index():
    return jsonify({
        "message": "Hello from Flask in Docker!",
        "port": PORT,
        "storage": STORAGE_DIR
    })

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    file.save(os.path.join(STORAGE_DIR, file.filename))
    return f"File {file.filename} uploaded", 200

@app.route('/files/<filename>')
def get_file(filename):
    path = os.path.join(STORAGE_DIR, filename)
    if os.path.exists(path):
        return send_file(path)
    return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)