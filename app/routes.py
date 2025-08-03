from flask import Blueprint, jsonify

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify([
        {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho"},
        {"id": 2, "title": "1984", "author": "George Orwell"},
        {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
    ])
