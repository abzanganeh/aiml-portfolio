#!/bin/bash

# Quick Fix Deployment Script
# Upload the working static site directly

echo "🚀 Quick fix deployment of static site..."

# Configuration
FTP_SERVER="srv637-files.hstgr.io"
REMOTE_DIR="/domains/zanganehai.com/public_html/"
LOCAL_DIR="static_site/"

# Check if lftp is installed
if ! command -v lftp &> /dev/null; then
    echo "❌ lftp is not installed. Installing..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install lftp
    fi
fi

# Get FTP credentials
echo "📝 Enter your FTP credentials to deploy working static files:"
read -p "FTP Username: " FTP_USERNAME
read -s -p "FTP Password: " FTP_PASSWORD
echo

echo "📁 Uploading static files to $FTP_SERVER$REMOTE_DIR..."

# Upload files using lftp
lftp -f "
open $FTP_SERVER
user $FTP_USERNAME $FTP_PASSWORD
lcd $LOCAL_DIR
cd $REMOTE_DIR
mirror --reverse --delete --verbose --exclude-glob .DS_Store
quit
"

if [ $? -eq 0 ]; then
    echo "✅ Quick fix deployment successful!"
    echo "🌐 Your portfolio should be working at https://zanganehai.com!"
else
    echo "❌ Quick fix deployment failed. Jenkins will handle the automatic deployment."
fi
