#!/bin/bash

# Push Deployment Fix Script
# v2.0803.1645 - Jenkins Pipeline Fix

echo "🚀 Pushing Jenkins Deployment Fix to GitHub"
echo "============================================"
echo ""

# Ensure we're in the right directory
cd "$(dirname "$0")"
echo "📁 Current directory: $(pwd)"
echo ""

# Check git status
echo "📋 Git Status:"
git status
echo ""

# Show what files have changed
echo "📝 Modified files:"
git diff --name-only
echo ""

# Add all changes
echo "➕ Adding all changes to git..."
git add .
echo ""

# Check what will be committed
echo "📦 Files to be committed:"
git diff --cached --name-only
echo ""

# Commit with detailed message
echo "💾 Committing changes..."
git commit -m "v2.0803.1645 - EMERGENCY: Fix Jenkins deployment pipeline

🔧 FIXES:
- Modified Jenkinsfile to deploy Flask app directly without static generation
- Removed dependency on generate_static.py script that was causing old deployments  
- Fixed pipeline to use current commit instead of old 93a42cc
- Updated version tracking to v2.0803.1645 with deployment fix description

🎯 IMPACT:
- Jenkins will now copy flask_portfolio/* directly to deployment/
- No more static site generation that was failing
- Eliminates confusion between static and dynamic sites
- Ensures current commit is deployed, not cached old commit

🚀 DEPLOYMENT:
- Pipeline simplified: checkout → copy Flask files → FTP deploy
- Should resolve zanganehai.com showing old content
- Version footer will show v2.0803.1645 when deployed"

echo ""

# Push to GitHub
echo "🚀 Pushing to GitHub main branch..."
git push origin main

echo ""

# Show the result
echo "✅ Push completed! Latest commit:"
git log --oneline -1
echo ""

# Final instructions
echo "🎯 NEXT STEPS:"
echo "1. Go to your Jenkins instance"
echo "2. Find the 'aiml-portfolio' job"  
echo "3. Click 'Build Now' to trigger deployment with new pipeline"
echo "4. Monitor the build - it should copy Flask files directly"
echo "5. Check zanganehai.com - should show Ali branding and v2.0803.1645"
echo ""
echo "🔍 VERIFICATION:"
echo "- Jenkins console should show 'Copying Flask application files...' instead of static generation"
echo "- Deployment directory should contain Flask templates, static files, etc."
echo "- Live site should reflect the updated content with correct branding"
echo ""
echo "📋 The key fix: Jenkins will use THIS commit instead of old 93a42cc"
