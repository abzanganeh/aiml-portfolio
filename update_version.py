#!/usr/bin/env python3
"""
Version Update Script for Portfolio Deployment
Automatically increments version number and updates build information
"""

import json
import os
import sys
from datetime import datetime

def load_version():
    """Load current version from version.json"""
    try:
        with open('version.json', 'r') as f:
            data = json.load(f)
            # Handle both old and new format
            if 'buildDate' in data:  # Old format
                return {
                    "version": data.get('version', '1.0.1'),
                    "build_id": data.get('buildId', 'initial'),
                    "build_date": data.get('buildDate', datetime.now().strftime("%Y-%m-%d")),
                    "description": data.get('description', 'Portfolio website'),
                    "changelog": data.get('changes', [])
                }
            return data  # New format
    except FileNotFoundError:
        return {
            "version": "2.0.0",
            "build_id": "20250803-0000",
            "build_date": datetime.now().strftime("%Y-%m-%d"),
            "description": "Second website iteration",
            "changelog": []
        }

def increment_version(current_version, increment_type='patch'):
    """Increment version number based on semantic versioning"""
    parts = current_version.split('.')
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    
    if increment_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif increment_type == 'minor':
        minor += 1
        patch = 0
    else:  # patch
        patch += 1
    
    return f"{major}.{minor}.{patch}"

def generate_build_id():
    """Generate unique build ID based on timestamp"""
    now = datetime.now()
    return now.strftime("%Y%m%d-%H%M")

def update_version_file(increment_type='patch', message='Automated deployment update'):
    """Update version.json with new version information"""
    
    # Load current version
    version_data = load_version()
    
    # Increment version
    current_version = version_data.get('version', '1.0.0')
    new_version = increment_version(current_version, increment_type)
    
    # Generate new build info
    build_id = generate_build_id()
    build_date = datetime.now().strftime("%Y-%m-%d")
    
    # Update version data
    version_data.update({
        "version": new_version,
        "build_id": build_id,
        "build_date": build_date,
        "description": "Portfolio website with version tracking",
        "last_updated": datetime.now().isoformat()
    })
    
    # Add to changelog
    if 'changelog' not in version_data:
        version_data['changelog'] = []
    
    version_data['changelog'].insert(0, {
        "version": new_version,
        "date": build_date,
        "changes": [message],
        "build_id": build_id
    })
    
    # Keep only last 10 changelog entries
    version_data['changelog'] = version_data['changelog'][:10]
    
    # Save updated version
    with open('version.json', 'w') as f:
        json.dump(version_data, f, indent=2)
    
    print(f"Version updated: {current_version} → {new_version}")
    print(f"Build ID: {build_id}")
    print(f"Build Date: {build_date}")
    
    return version_data

def main():
    """Main function to handle command line arguments"""
    increment_type = 'patch'  # default
    message = 'Automated deployment update'
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        increment_type = sys.argv[1].lower()
        if increment_type not in ['major', 'minor', 'patch']:
            print("Error: increment_type must be 'major', 'minor', or 'patch'")
            sys.exit(1)
    
    if len(sys.argv) > 2:
        message = ' '.join(sys.argv[2:])
    
    # Update version
    try:
        version_data = update_version_file(increment_type, message)
        print("Version update successful!")
        print(f"New version: {version_data['version']}")
        
        # Display changelog
        if version_data.get('changelog'):
            print("\nRecent changes:")
            for entry in version_data['changelog'][:3]:
                print(f"  v{entry['version']} ({entry['date']}): {', '.join(entry['changes'])}")
                
    except Exception as e:
        print(f"Error updating version: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
