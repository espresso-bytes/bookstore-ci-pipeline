from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 📦 Convert price to INR if sale info is available
def get_price(item):
    sale_info = item.get("saleInfo", {})
    if sale_info.get("saleability") == "FOR_SALE":
        amount = sale_info["retailPrice"]["amount"]
        currency = sale_info["retailPrice"]["currencyCode"]
        if currency != "INR":
            # Example conversion rate (you can integrate a live API for this)
            conversion_rate = 80  # USD to INR approx
            amount *= conversion_rate
        return f"{round(amount)} INR"
    else:
        return "Not for Sale"

# 📚 Fetch books from Google Books API
def fetch_books_from_google(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=20"
    response = requests.get(url)
    items = response.json().get("items", [])

    books = []
    for item in items:
        volume_info = item.get("volumeInfo", {})
        books.append({
            "title": volume_info.get("title", "No Title"),
            "authors": ", ".join(volume_info.get("authors", ["Unknown"])),
            "rating": volume_info.get("averageRating", 0),
            "thumbnail": volume_info.get("imageLinks", {}).get("thumbnail"),
            "price": get_price(item),
        })
    return books

# 🧠 Main route with search + filter
@app.route("/", methods=["GET"])
def index():
    search_query = request.args.get("search", "").strip()
    selected_filter = request.args.get("filter", "none")

    if search_query:
        books = fetch_books_from_google(search_query)
    else:
        books = fetch_books_from_google("bestsellers")

    if selected_filter == "high_rating":
        books = sorted(books, key=lambda x: x.get("rating", 0), reverse=True)
    elif selected_filter == "low_price":
        books = sorted(
            books,
            key=lambda x: float(x["price"].split()[0])
            if x["price"] != "Not for Sale"
            else float("inf"),
        )

    return render_template("books.html", books=books, search_query=search_query, selected_filter=selected_filter)

# 🚀 Start Flask app
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
