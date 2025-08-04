# 403 Forbidden Error Troubleshooting Guide

## Quick Diagnosis

If you're getting 403 Forbidden errors when clicking the tutorial menu, here are the most common causes and solutions:

## 🔍 Step 1: Test Locally First

```bash
# Run this from the WebSite directory
./fix_403_errors.sh
```

Then test at: `http://localhost:8000`

## 🌐 Step 2: Check Your Deployed Server

### Common Issues on Web Servers:

#### A. File Permissions (Most Common)
```bash
# On your server, set correct permissions:
find /path/to/your/site -type f -name "*.html" -exec chmod 644 {} \;
find /path/to/your/site -type d -exec chmod 755 {} \;
```

#### B. Missing Directory Index Files
Some servers require `index.html` in every directory. Add these files:
- `tutorials/index.html` (redirects to main tutorials page)
- `projects/index.html` (redirects to main projects page)

#### C. Server Configuration Issues

**For Apache (.htaccess):**
```apache
# Allow access to HTML files
<Files "*.html">
    Order allow,deny
    Allow from all
</Files>

# Enable directory indexing (if needed)
Options +Indexes
```

**For Nginx:**
```nginx
location / {
    try_files $uri $uri/ /index.html;
}

location ~* \.(html|css|js|png|jpg|jpeg|gif|svg)$ {
    expires 1M;
    add_header Cache-Control "public, immutable";
}
```

## 🔧 Step 3: Deployment-Specific Fixes

### GitHub Pages
- Ensure all files are in the `docs/` folder or root of `gh-pages` branch
- Check repository settings for proper source configuration

### Netlify/Vercel
- Add a `_redirects` file:
```
/tutorials /tutorials.html 200
/projects /projects.html 200
/* /index.html 200
```

### Traditional Web Hosting
1. Upload all files via FTP/SFTP
2. Ensure directory structure is preserved:
   ```
   public_html/
   ├── index.html
   ├── tutorials.html
   ├── projects.html
   ├── static/
   │   ├── css/
   │   ├── js/
   │   └── images/
   ├── tutorials/
   └── projects/
   ```
3. Set permissions: directories 755, files 644

## 🚨 Emergency Fix

If you're still getting 403 errors, try this minimal test:

1. Create a simple `test.html` file in your web root:
```html
<!DOCTYPE html>
<html><head><title>Test</title></head>
<body><h1>Server is working!</h1></body></html>
```

2. If `test.html` works but `tutorials.html` doesn't:
   - The issue is with the specific file
   - Check file encoding (should be UTF-8)
   - Check for special characters in file content

3. If `test.html` also gives 403:
   - The issue is server configuration
   - Contact your hosting provider
   - Check server error logs

## 📞 Getting Help

If none of these solutions work:

1. **Check server error logs** for specific error messages
2. **Contact your hosting provider** with this information:
   - Error message: "403 Forbidden"
   - Affected files: tutorials.html, projects.html
   - File permissions: 644 for files, 755 for directories
3. **Provide them with the file structure** from this repository

## ✅ Verification

After applying fixes, test these URLs:
- `/` (should show homepage)
- `/tutorials.html` (should show tutorials page)
- `/projects.html` (should show projects page)
- `/tutorials/data-preprocessing.html` (should show the interactive tutorial)

## 🔄 Automated Solution

For future deployments, the `serve_static.py` script in this repository provides a reliable local server that handles all these issues automatically.
