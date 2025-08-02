#!/usr/bin/env python3
"""
Simple HTTP server to serve the static portfolio site.
Run this script to serve the static_site directory.
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Get the directory containing this script
SCRIPT_DIR = Path(__file__).parent.absolute()
STATIC_SITE_DIR = SCRIPT_DIR / "static_site"

def serve_static_site(port=8000):
    """Serve the static site on the specified port"""
    
    if not STATIC_SITE_DIR.exists():
        print(f"Error: Static site directory not found at {STATIC_SITE_DIR}")
        sys.exit(1)
    
    # Change to the static site directory
    os.chdir(STATIC_SITE_DIR)
    
    # Create a simple HTTP request handler
    class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            # Add CORS headers for local development
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', '*')
            super().end_headers()
        
        def do_GET(self):
            # Handle root path
            if self.path == '/':
                self.path = '/index.html'
            return super().do_GET()
    
    # Start the server
    with socketserver.TCPServer(("", port), HTTPRequestHandler) as httpd:
        print(f"Serving static portfolio at http://localhost:{port}")
        print(f"Static site directory: {STATIC_SITE_DIR}")
        print("Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8000.")
    
    serve_static_site(port)
