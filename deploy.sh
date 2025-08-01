#!/bin/bash

# Manual Deployment Script
# Run this script to manually deploy to your web server

echo "🚀 Starting manual deployment to web server..."

# Configuration
FTP_SERVER="srv637-files.hstgr.io"
REMOTE_DIR="/public_html/"
LOCAL_DIR="./"

# Check if lftp is installed
if ! command -v lftp &> /dev/null; then
    echo "❌ lftp is not installed. Installing..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        brew install lftp
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        sudo apt-get update && sudo apt-get install -y lftp
    else
        echo "Please install lftp manually and run this script again."
        exit 1
    fi
fi

# Get FTP credentials
echo "📝 Enter your FTP credentials:"
read -p "FTP Username: " FTP_USERNAME
read -s -p "FTP Password: " FTP_PASSWORD
echo

echo "📁 Uploading files to $FTP_SERVER$REMOTE_DIR..."

# Upload files using lftp
lftp -f "
open $FTP_SERVER
user $FTP_USERNAME $FTP_PASSWORD
lcd $LOCAL_DIR
cd $REMOTE_DIR
mirror --reverse --delete --verbose --exclude-glob .git* --exclude-glob .DS_Store --exclude-glob README.md --exclude-glob .github/ --exclude-glob DEPLOYMENT.md --exclude-glob deploy.sh
quit
"

if [ $? -eq 0 ]; then
    echo "✅ Deployment successful!"
    echo "🌐 Your portfolio should be live at your domain!"
else
    echo "❌ Deployment failed. Please check your credentials and server settings."
    exit 1
fi
