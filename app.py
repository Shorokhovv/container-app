import os
from flask import Flask, jsonify

app = Flask(__name__)
PORT = int(os.environ.get("APP_PORT", 8000))

@app.route('/')
def index():
    return jsonify({
        "message": "Hello from Flask in Docker!",
        "port": PORT
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
