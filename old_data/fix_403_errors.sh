#!/bin/bash

# Fix 403 Forbidden Issues for Static Portfolio Site
# This script addresses common causes of 403 errors

echo "🔧 Fixing 403 Forbidden Issues..."

# Check if we're in the correct directory
if [ ! -f "static_site/index.html" ]; then
    echo "❌ Error: Please run this script from the WebSite root directory"
    exit 1
fi

# Navigate to static site directory
cd static_site

echo "📁 Current directory: $(pwd)"
echo "📄 Files in directory:"
ls -la

echo ""
echo "🔒 Fixing file permissions..."

# Set correct permissions for files and directories
find . -type f -name "*.html" -exec chmod 644 {} \;
find . -type f -name "*.css" -exec chmod 644 {} \;
find . -type f -name "*.js" -exec chmod 644 {} \;
find . -type f -name "*.png" -exec chmod 644 {} \;
find . -type f -name "*.jpg" -exec chmod 644 {} \;
find . -type f -name "*.jpeg" -exec chmod 644 {} \;
find . -type f -name "*.svg" -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;

echo "✅ File permissions updated"

echo ""
echo "🌐 Testing file accessibility..."

# Test if key files exist and are readable
test_files=("index.html" "tutorials.html" "projects.html" "tutorials/data-preprocessing.html")

for file in "${test_files[@]}"; do
    if [ -f "$file" ]; then
        if [ -r "$file" ]; then
            echo "✅ $file - exists and readable"
        else
            echo "❌ $file - exists but not readable"
            chmod 644 "$file"
        fi
    else
        echo "❌ $file - missing"
    fi
done

echo ""
echo "📊 Directory structure:"
tree -L 2 2>/dev/null || find . -type d | head -20

echo ""
echo "🚀 Starting test server..."

# Kill any existing servers on port 8000
lsof -ti:8000 | xargs kill -9 2>/dev/null || true

# Start a simple HTTP server for testing
echo "Starting server at http://localhost:8000"
echo "Press Ctrl+C to stop the server"
echo ""

python3 -m http.server 8000 2>/dev/null || python -m http.server 8000
