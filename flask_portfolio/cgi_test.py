#!/usr/bin/env python3

print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
print("<html><head><title>Python CGI Test</title></head>")
print("<body>")
print("<h1>✅ Python CGI is Working!</h1>")
print("<p>If you see this, Python CGI execution is working on your server.</p>")
print("<p>Server info:</p>")
print("<ul>")

import sys
print(f"<li>Python version: {sys.version}</li>")

try:
    import os
    print(f"<li>Current directory: {os.getcwd()}</li>")
    print(f"<li>Environment: CGI={os.environ.get('REQUEST_METHOD', 'Not CGI')}</li>")
except:
    print("<li>OS module not available</li>")

try:
    import flask
    print(f"<li>✅ Flask available: {flask.__version__}</li>")
except ImportError:
    print("<li>❌ Flask not available</li>")

print("</ul>")
print("</body></html>")
