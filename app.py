from flask import Flask, jsonify
from flask_cors import CORS
from logic import Book

app = Flask(__name__)
CORS(app)

new_book = Book(title="1984", author="George Orwell", publish_year=1949)

dict_book = new_book.to_dict()

@app.route('/')
def home():
    return jsonify(book= dict_book)

if __name__ == '__main__':
    app.run(debug=True)
