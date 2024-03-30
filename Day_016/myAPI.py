#!/usr/bin/env python3
"""Module with RESTful API endpoints for a given bookstore"""


from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory database)
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"}
]
next_id = 4

# GET /books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET /books/{id}
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# POST /books
@app.route('/books', methods=['POST'])
def add_book():
    global next_id
    data = request.json
    new_book = {"id": next_id, "title": data["title"], "author": data["author"]}
    books.append(new_book)
    next_id += 1
    return jsonify(new_book), 201

# PUT /books/{id}
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book['title'] = data['title']
        book['author'] = data['author']
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# DELETE /books/{id}
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

