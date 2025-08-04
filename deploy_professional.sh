#!/bin/bash

# Professional Flask Portfolio Deployment
# Ali Barzin Zanganeh - Machine Learning Engineer Portfolio
# Single, clean deployment script

echo "🚀 Professional Flask Portfolio Deployment"
echo "==========================================="
echo ""

# Verify we're in the right directory
if [ ! -f "version.json" ]; then
    echo "❌ Error: Not in the correct project directory"
    echo "Please run this script from the WebSite root directory"
    exit 1
fi

# Check git status
echo "📋 Checking git status..."
git status --porcelain

echo ""

# Add all changes
echo "➕ Adding changes to git..."
git add .

# Get current version
VERSION=$(grep '"version"' version.json | cut -d'"' -f4)
echo "📦 Current version: $VERSION"

# Commit with professional message
echo "💾 Committing professional Flask application..."
git commit -m "$VERSION - Professional Flask application deployment

🏆 FEATURES:
- Flask application with WSGI/CGI auto-detection
- Professional .htaccess configuration
- Security headers and performance optimization
- Clean, maintainable codebase

🔧 TECHNICAL:
- Automatic environment detection (CGI/dev server)
- Professional URL routing and error handling
- Optimized static asset serving
- Security headers implementation

🚀 DEPLOYMENT:
- Single professional solution
- Compatible with shared hosting
- Production-ready configuration"

echo ""

# Push to GitHub to trigger Jenkins
echo "🚀 Deploying to production via Jenkins..."
git push origin main

echo ""
echo "✅ DEPLOYMENT INITIATED!"
echo ""
echo "🎯 WHAT HAPPENS NEXT:"
echo "1. GitHub receives the push"
echo "2. Jenkins automatically triggers build"
echo "3. Professional Flask app deployed to server"
echo "4. Live site updated at zanganehai.com"
echo ""
echo "📱 Features deployed:"
echo "- Professional Flask application"
echo "- WSGI/CGI support for shared hosting"
echo "- Security headers and performance optimization"
echo "- Clean URL routing and error handling"
echo ""
echo "� Monitor deployment:"
echo "- Check Jenkins console for build status"
echo "- Verify live site shows version: $VERSION"
