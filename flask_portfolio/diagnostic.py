#!/usr/bin/env python3
"""
Diagnostic Flask Application
Simple version to test CGI execution and identify 500 errors
"""

import os
import sys
import traceback
from datetime import datetime

def application(environ, start_response):
    """Simple WSGI application for debugging"""
    try:
        # Basic HTML response
        response_body = f"""<!DOCTYPE html>
<html>
<head>
    <title>Diagnostic - Ali Barzin Zanganeh</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 2rem; }}
        .success {{ color: green; }}
        .error {{ color: red; }}
        .info {{ background: #f0f0f0; padding: 1rem; margin: 1rem 0; }}
    </style>
</head>
<body>
    <h1>🔧 Diagnostic Mode - Ali Barzin Zanganeh Portfolio</h1>
    
    <div class="success">
        <h2>✅ Python CGI Working!</h2>
        <p>This means the server can execute Python scripts.</p>
    </div>
    
    <div class="info">
        <h3>📋 System Information:</h3>
        <ul>
            <li><strong>Python Version:</strong> {sys.version}</li>
            <li><strong>Current Time:</strong> {datetime.now()}</li>
            <li><strong>Working Directory:</strong> {os.getcwd()}</li>
            <li><strong>Script Path:</strong> {__file__ if '__file__' in globals() else 'Unknown'}</li>
        </ul>
    </div>
    
    <div class="info">
        <h3>🌍 Environment Variables:</h3>
        <ul>
            <li><strong>REQUEST_METHOD:</strong> {environ.get('REQUEST_METHOD', 'Not Set')}</li>
            <li><strong>SERVER_NAME:</strong> {environ.get('SERVER_NAME', 'Not Set')}</li>
            <li><strong>SCRIPT_NAME:</strong> {environ.get('SCRIPT_NAME', 'Not Set')}</li>
        </ul>
    </div>
    
    <div class="info">
        <h3>📁 Available Files:</h3>
        <ul>
        {"".join([f"<li>{file}</li>" for file in os.listdir('.') if not file.startswith('.')])}
        </ul>
    </div>
    
    <div style="margin-top: 2rem; padding: 1rem; background: #e8f5e8;">
        <h3>🎯 Next Steps:</h3>
        <p>If you see this page, CGI is working. The main Flask app might have dependency issues.</p>
        <p>Try installing Flask dependencies or check error logs.</p>
    </div>
    
    <footer style="margin-top: 3rem; border-top: 1px solid #ccc; padding-top: 1rem;">
        <p><em>Diagnostic Mode - Ali Barzin Zanganeh Portfolio v2.0803.1715</em></p>
    </footer>
</body>
</html>"""
        
        status = '200 OK'
        headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
            ('Content-Length', str(len(response_body.encode('utf-8'))))
        ]
        
        start_response(status, headers)
        return [response_body.encode('utf-8')]
        
    except Exception as e:
        # Error response
        error_body = f"""<!DOCTYPE html>
<html>
<head><title>Error - Diagnostic</title></head>
<body>
    <h1>❌ Error in Diagnostic Mode</h1>
    <p><strong>Error:</strong> {str(e)}</p>
    <pre>{traceback.format_exc()}</pre>
</body>
</html>"""
        
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        return [error_body.encode('utf-8')]

if __name__ == '__main__':
    # Check if running as CGI
    if 'REQUEST_METHOD' in os.environ:
        # Running as CGI script
        from wsgiref.handlers import CGIHandler
        CGIHandler().run(application)
    else:
        # Running locally for testing
        print("Content-Type: text/html\\n")
        print("This is diagnostic mode. Upload to server to test CGI.")
