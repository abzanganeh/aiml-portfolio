#!/usr/bin/env python3
"""
Start the Flask portfolio application.
This script makes it easy to run the Flask app with proper configuration.
"""

import os
import sys
from pathlib import Path

# Add the flask_portfolio directory to the Python path
SCRIPT_DIR = Path(__file__).parent.absolute()
FLASK_DIR = SCRIPT_DIR / "flask_portfolio"

if not FLASK_DIR.exists():
    print(f"Error: Flask directory not found at {FLASK_DIR}")
    sys.exit(1)

# Change to the Flask directory
os.chdir(FLASK_DIR)
sys.path.insert(0, str(FLASK_DIR))

# Import and run the Flask app
try:
    from app import app
    
    print("Starting Flask Portfolio Application...")
    print("Flask directory:", FLASK_DIR)
    print("Access the portfolio at: http://localhost:5001")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Run the Flask app
    app.run(
        debug=True,
        host='127.0.0.1',
        port=5001
    )
    
except ImportError as e:
    print(f"Error importing Flask app: {e}")
    print("Make sure all dependencies are installed:")
    print("pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"Error starting Flask app: {e}")
    sys.exit(1)
