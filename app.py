from flask import Flask, send_file
import os

# Get the absolute path to the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=BASE_DIR, static_url_path='')

@app.route('/')
def serve_index():
    return send_file(os.path.join(BASE_DIR, 'index.html'))

@app.route('/<path:path>')
def serve_file(path):
    file_path = os.path.join(BASE_DIR, path)
    if os.path.isfile(file_path):
        return send_file(file_path)
    # If file not found, serve index.html
    return send_file(os.path.join(BASE_DIR, 'index.html'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
