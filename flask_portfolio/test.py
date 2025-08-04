#!/usr/bin/env python3

# Minimal CGI Test - No imports, no dependencies
print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html>
<head>
    <title>Minimal CGI Test</title>
    <style>
        body { font-family: Arial; margin: 2rem; background: #f0f8ff; }
        .success { color: green; font-size: 1.5rem; }
    </style>
</head>
<body>
    <h1 class="success">✅ BASIC CGI WORKS!</h1>
    <p>If you see this page, Python CGI execution is working on the server.</p>
    <p><strong>This means the 500 error is caused by:</strong></p>
    <ul>
        <li>Missing Python modules (Flask, etc.)</li>
        <li>Import errors in the main app</li>
        <li>File permissions or path issues</li>
    </ul>
    <hr>
    <p><em>Minimal CGI Test - Ali Barzin Zanganeh Portfolio</em></p>
</body>
</html>""")
