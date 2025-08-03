from flask import Blueprint, render_template, request
import requests

books_bp = Blueprint('books', __name__)

def fetch_books(query="python"):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)
    if response.status_code != 200:
        return []
    
    data = response.json()
    books = []
    for item in data.get('items', []):
        volume = item.get('volumeInfo', {})
        sale = item.get('saleInfo', {})
        price = sale.get('listPrice', {}).get('amount', 'N/A')
        currency = sale.get('listPrice', {}).get('currencyCode', '')
        
        books.append({
            'title': volume.get('title'),
            'authors': ", ".join(volume.get('authors', [])),
            'rating': volume.get('averageRating', 0),
            'thumbnail': volume.get('imageLinks', {}).get('thumbnail'),
            'price': f"{price} {currency}" if price != 'N/A' else "Not for Sale"
        })
    return books

@books_bp.route('/', methods=['GET'])
def home():
    search_query = request.args.get('search', 'python')
    filter_option = request.args.get('filter', 'none')
    books = fetch_books(search_query)

    if filter_option == 'high_rating':
        books.sort(key=lambda x: x.get('rating', 0), reverse=True)
    elif filter_option == 'low_price':
        books = [b for b in books if isinstance(b.get('price'), str) and b['price'] != 'Not for Sale']
        books.sort(key=lambda x: float(x['price'].split()[0]))

    return render_template('books.html', books=books, search_query=search_query, selected_filter=filter_option)
