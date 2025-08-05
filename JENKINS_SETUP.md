# Jenkins Setup Documentation

## Overview
This document outlines the Jenkins CI/CD pipeline setup for the Ali Zanganeh AIML Portfolio.

## Pipeline Configuration
- **Pipeline Name**: website-portfolio-deployment
- **Trigger**: GitHub webhook on push to main branch
- **Agent**: macOS agent (macos-agent)
- **Deployment Target**: srv637-files.hstgr.io

## Deployment Process
1. Code checkout from GitHub repository
2. File validation and preprocessing
3. FTP deployment via lftp to hosting server
4. Deployment verification and status reporting

## Server Details
- **FTP Server**: srv637-files.hstgr.io
- **Target Directory**: /domains/zanganehai.com/public_html/
- **Protocol**: FTP with lftp client

## Status
✅ Jenkins pipeline operational and working
✅ Dual deployment with GitHub Actions
✅ Auto-deployment on code changes
