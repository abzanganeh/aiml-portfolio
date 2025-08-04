#!/bin/bash

# Portfolio Deployment Script with Version Tracking
# This script automates the deployment process with automatic version updates

set -e  # Exit on any error

echo "=== Portfolio Deployment with Version Tracking ==="
echo "Starting deployment process..."

# Check if we're in the correct directory
if [ ! -f "version.json" ]; then
    echo "Error: version.json not found. Are you in the correct directory?"
    exit 1
fi

# Parse command line arguments
INCREMENT_TYPE="patch"
COMMIT_MESSAGE="Deployment update"

while [[ $# -gt 0 ]]; do
    case $1 in
        --version-type)
            INCREMENT_TYPE="$2"
            shift 2
            ;;
        --message)
            COMMIT_MESSAGE="$2"
            shift 2
            ;;
        --help)
            echo "Usage: $0 [--version-type major|minor|patch] [--message 'commit message']"
            echo "  --version-type: Type of version increment (default: patch)"
            echo "  --message: Git commit message (default: 'Deployment update')"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Validate version type
if [[ ! "$INCREMENT_TYPE" =~ ^(major|minor|patch)$ ]]; then
    echo "Error: version-type must be 'major', 'minor', or 'patch'"
    exit 1
fi

echo "Configuration:"
echo "  Version increment: $INCREMENT_TYPE"
echo "  Commit message: $COMMIT_MESSAGE"
echo ""

# Update version number
echo "Step 1: Updating version number..."
python3 update_version.py "$INCREMENT_TYPE" "$COMMIT_MESSAGE"

if [ $? -ne 0 ]; then
    echo "Error: Failed to update version"
    exit 1
fi

# Get the new version for commit message
NEW_VERSION=$(python3 -c "
import json
with open('version.json', 'r') as f:
    data = json.load(f)
print(data['version'])
")

echo "Updated to version: $NEW_VERSION"
echo ""

# Add files to git
echo "Step 2: Adding files to git..."
git add version.json
git add .

# Commit changes
echo "Step 3: Committing changes..."
FULL_COMMIT_MESSAGE="v$NEW_VERSION: $COMMIT_MESSAGE"
git commit -m "$FULL_COMMIT_MESSAGE"

echo "Step 4: Pushing to repository..."
git push origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=== Deployment Complete ==="
    echo "✅ Version updated to: v$NEW_VERSION"
    echo "✅ Changes committed and pushed"
    echo "✅ Version tracking enabled in footer"
    echo ""
    echo "You can now check the deployed site footer to verify the deployment!"
    echo "Look for: Version: v$NEW_VERSION"
else
    echo "❌ Error: Failed to push to repository"
    exit 1
fi
