from flask import Flask, jsonify
from flask_cors import CORS
from logic import Book
import json

app = Flask(__name__)
CORS(app)

with open('books.json', 'r') as file:
    books_data = json.load(file)

book_objs = []
for book in books_data['books']:
    new_book = Book(
        title = book['title'],
        author = book['authors'],
        publish_year = int(book.get('publish_year', 0)),
        isbn = book.get('isbn'),
        image = book['image']
    )
    book_objs.append(new_book)

books_dicts = [book.to_dict() for book in book_objs]

@app.route('/', methods=['GET'])
def get_books():
    return jsonify(books = books_dicts)

if __name__ == '__main__':
    app.run(debug=True)
