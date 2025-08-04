#!/bin/bash
# Emergency deployment fix script
# This script commits the Jenkins pipeline fix and forces a new deployment

echo "🔧 Emergency Deployment Fix - v2.0803.1645"
echo "============================================"

# Check git status
echo "📋 Checking git status..."
git status

# Add all changes
echo "📁 Adding changes to git..."
git add .

# Commit with clear message
echo "💾 Committing changes..."
git commit -m "v2.0803.1645 - EMERGENCY: Fix Jenkins deployment pipeline

- Modified Jenkinsfile to deploy Flask app directly without static generation
- Removed dependency on generate_static.py script that was causing old deployments
- Fixed pipeline to use current commit instead of old 93a42cc
- Updated version tracking with deployment fix
- This should resolve the issue where Jenkins was deploying from old commit"

# Push to main branch
echo "🚀 Pushing to GitHub..."
git push origin main

# Show the latest commit
echo "✅ Latest commit:"
git log --oneline -1

echo ""
echo "🎯 Next steps:"
echo "1. Go to Jenkins and trigger a new build manually"
echo "2. The new pipeline should deploy Flask files directly"
echo "3. Check zanganehai.com to verify the new deployment"
echo ""
echo "The new pipeline will copy flask_portfolio/* to deployment/ instead of generating static files"
