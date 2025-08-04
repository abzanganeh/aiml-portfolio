# Portfolio Deployment Guide

## 🚨 Fixing 403 Forbidden Errors

The 403 Forbidden error occurs when trying to access files that the web server can't serve properly. Here are solutions:

## Option 1: Flask Application (Recommended)

Run the Flask application which handles routing properly:

```bash
# Install dependencies
cd flask_portfolio
pip install -r requirements.txt

# Run the Flask app
python app.py
```

Then access: `http://localhost:5001`

## Option 2: Static Site with HTTP Server

For the static site, you need a proper HTTP server:

```bash
# Using Python's built-in server
cd static_site
python -m http.server 8000
```

Then access: `http://localhost:8000`

## Option 3: Using the Helper Scripts

We've created helper scripts:

```bash
# For Flask app
python run_flask.py

# For static site
python serve_static.py
```

## 🔧 Common Issues:

1. **403 Forbidden**: Usually means trying to access files directly in browser
2. **File not found**: Check that you're in the correct directory
3. **Permission denied**: Make sure scripts are executable

## 📁 Directory Structure:

```
WebSite/
├── flask_portfolio/     # Flask application (dynamic)
│   ├── app.py
│   ├── static/
│   └── templates/
├── static_site/         # Static HTML files
│   ├── index.html
│   ├── tutorials.html
│   ├── projects.html
│   └── static/
├── run_flask.py         # Helper to run Flask app
└── serve_static.py      # Helper to serve static site
```

## 🚀 For Production:

- Flask app: Use Gunicorn or similar WSGI server
- Static site: Use Nginx, Apache, or GitHub Pages
- Both: Upload to hosting service with proper configuration
