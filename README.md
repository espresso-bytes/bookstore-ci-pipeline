# 📚 Bookstore API Dashboard - Flask + Docker + CI/CD

A smart Flask web app to display books using the **Google Books API**, styled beautifully and built with an end-to-end **CI/CD pipeline using Docker & GitHub Actions**.

---

## 🚀 Project Overview

This project demonstrates a modern workflow for deploying Python web apps:
- Flask web app fetching live book data
- Dockerized for consistent builds
- CI/CD pipeline using GitHub Actions
- (Optional) Hosted on Render / Railway / Fly.io

---

## 🔧 Tech Stack

| Layer        | Tool/Tech         |
|--------------|------------------|
| Backend      | Python, Flask     |
| External API | Google Books API  |
| Frontend     | Jinja2 Templates (HTML + CSS) |
| Container    | Docker            |
| CI/CD        | GitHub Actions    |
| Deployment   | Render (or your choice) |

---

## 🛠 How It Was Built
### 1️⃣ Flask App First
- Built a Python Flask app that:
  - Accepts user input to search books.
  - Calls **Google Books API**.
  - Displays live book info (title, authors, rating, image, price).
- Used basic HTML templates via Jinja2.
📁 Key files:
- `run.py` → Flask server
- `templates/books.html` → UI page
- `requirements.txt` → Dependencies
---
### 2️⃣ Dockerized the App
- Created a `Dockerfile` to containerize the app.
- Ensured it runs on `0.0.0.0:5000` for external access.
📁 Key files:
- `Dockerfile`
- `.dockerignore`

🧪 To run locally:
bash:-
 - docker build -t flask-bookstore .
 - docker run -p 5000:5000 flask-bookstore

## CI/CD Pipeline with GitHub Actions
Set up .github/workflows/main.yml for CI/CD:
<img width="1914" height="861" alt="image" src="https://github.com/user-attachments/assets/f613deb7-ce98-45c3-9b61-2a0cc202cf4c" />

Every push triggers:
 - Code Linting
 - Docker Build
 - Container Test Run

## 📷 Snapshots of GitHub Actions will be added here

<img width="1912" height="812" alt="Screenshot 2025-08-04 044707" src="https://github.com/user-attachments/assets/0824a5dd-ee97-4df3-80a5-94a3c8f458ab" />
<img width="1906" height="984" alt="Screenshot 2025-08-04 044700" src="https://github.com/user-attachments/assets/b6b9200c-8e86-4313-9117-f7d46eaea7ec" />
<img width="1882" height="965" alt="Screenshot 2025-08-04 051148" src="https://github.com/user-attachments/assets/328a429a-35d2-418a-aada-96481b31aad7" />


## 🧪 Features
✅ Live Book Search
✅ Google Books API integration
✅ Dockerized Application
✅ GitHub Actions for CI
✅ Search by Title/Author
✅ Shows Rating & Price (INR)

📝 License
MIT License<License> 
