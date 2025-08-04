#!/bin/bash

# Professional Static HTML Portfolio Deployment
# Ali Barzin Zanganeh - Machine Learning Engineer Portfolio  
# Version 3.0 - Complete static website deployment

echo "🚀 Professional Static HTML Portfolio Deployment v3.0"
echo "======================================================"
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
echo "💾 Committing professional static HTML website v3.0..."
git commit -m "$VERSION - Professional Static HTML Website v3.0

🏆 FEATURES:
- Complete static HTML/CSS/JavaScript website
- Professional responsive design with modern animations
- Comprehensive machine learning tutorial collection
- Mobile-first responsive layout

🔧 TECHNICAL:
- Static HTML architecture for universal hosting compatibility
- Professional CSS Grid/Flexbox layouts
- Vanilla JavaScript with modern browser APIs
- Optimized performance and security headers

🚀 DEPLOYMENT:
- Static website deployment via Jenkins
- Compatible with all hosting providers
- Fast loading and SEO optimized"

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
