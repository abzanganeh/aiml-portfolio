#!/bin/bash

echo "🧹 FINAL CLEANUP & RESTART - v2.0803.1630"
echo "=========================================="

# Remove static site confusion
echo "📁 Removing static site files..."
rm -rf static_site/
rm -f generate_static.py serve_static.py

# Show final structure
echo "📋 Final project structure:"
echo "✅ flask_portfolio/ (main app)"
echo "✅ run_flask.py (launcher)"  
echo "✅ version.json (v2.0803.1630)"
echo "✅ README.md (updated)"

# Test Flask app
echo ""
echo "🚀 Testing Flask application..."
echo "Starting server on http://localhost:5001"
echo "Press Ctrl+C to stop"
echo ""

cd flask_portfolio && python3 app.py
