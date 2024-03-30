#!/usr/bin/env python3
"""Module with RESTful API endpoints for a given bookstore
and includes Filtering, Sorting, and Pagination """

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
    # Retrieve query parameters
    search_query = request.args.get('q')
    sort_by = request.args.get('sort')
    author_filter = request.args.get('author')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))

    # Apply searching
    if search_query:
        books_filtered = [book for book in books if search_query.lower() in book['title'].lower() or search_query.lower() in book['author'].lower()]
    else:
        books_filtered = books.copy()

    # Apply filtering
    if author_filter:
        books_filtered = [book for book in books_filtered if author_filter.lower() == book['author'].lower()]

    # Apply sorting
    if sort_by:
        books_filtered.sort(key=lambda x: x.get(sort_by, ''), reverse=('desc' in sort_by))

    # Apply pagination
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    books_paginated = books_filtered[start_index:end_index]

    return jsonify(books_paginated)

if __name__ == '__main__':
    app.run(debug=True)
