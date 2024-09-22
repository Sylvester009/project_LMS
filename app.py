from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify(message='Welcome to the LMS visitor page!')

@app.route('/member')
def member():
    return jsonify(message='Welcome to the LMS member page!')

@app.route('/librarian')
def librarian():
    return jsonify(message='Welcome to the LMS librarian page!')

if __name__ == '__main__':
    app.run(debug=True)
