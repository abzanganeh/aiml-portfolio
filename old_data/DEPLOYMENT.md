# Deployment Setup Guide

## GitHub Actions Auto-Deployment

This repository is configured to automatically deploy to your web server (`https://srv637-files.hstgr.io/54b7d1bc1ec58d94/files/public_html/`) whenever you push to the `main` branch.

## Required GitHub Secrets

You need to add the following secrets to your GitHub repository:

### Go to: `https://github.com/abzanganeh/aiml-portfolio/settings/secrets/actions`

#### FTP Deployment Secrets:
1. **FTP_SERVER**: `srv637-files.hstgr.io` (or your FTP server address)
2. **FTP_USERNAME**: Your FTP username
3. **FTP_PASSWORD**: Your FTP password

#### Alternative SFTP Deployment Secrets (backup method):
1. **SFTP_HOST**: Your SFTP server hostname
2. **SFTP_USERNAME**: Your SFTP username  
3. **SFTP_PRIVATE_KEY**: Your private SSH key (if using key-based auth)

## How to Add Secrets:

1. Go to your repository: `https://github.com/abzanganeh/aiml-portfolio`
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret with its name and value

## Deployment Process:

1. **Push to GitHub**: Any push to `main` branch triggers deployment
2. **Automatic Upload**: Files are uploaded to `/public_html/` on your server
3. **Live Updates**: Your website is automatically updated
4. **Manual Trigger**: You can also manually trigger deployment from Actions tab

## Excluded Files:

The following files won't be uploaded to your server:
- `.git` folders and files
- `node_modules/`
- `.DS_Store` (Mac files)
- `.gitignore`
- `README.md`
- `.github/` workflow files

## Testing:

After setting up secrets, make a small change and push to test the deployment.

## Server Details:

- **Target Directory**: `/public_html/`
- **Server**: `srv637-files.hstgr.io`
- **Expected URL**: Your domain pointing to this server

## Troubleshooting:

- Check the Actions tab for deployment logs
- Verify FTP credentials are correct
- Ensure server directory permissions allow uploads
- Contact hosting provider if FTP access issues persist
