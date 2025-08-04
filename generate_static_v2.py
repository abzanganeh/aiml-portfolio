#!/usr/bin/env python3
"""
Static Site Generator for Flask Portfolio
Converts the Flask application to static HTML files for shared hosting
"""

import os
import sys
import json
from urllib.parse import urljoin
from flask import Flask, render_template, url_for
from flask_portfolio.app import create_app
from flask_portfolio.models.project import projects
from flask_portfolio.models.tutorial import tutorials

# Add the flask_portfolio directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'flask_portfolio'))

def generate_static_site():
    """Generate static HTML files from Flask application"""
    
    # Create Flask app
    app = create_app()
    
    # Output directory for static files
    output_dir = 'static_site'
    
    # Remove existing output directory
    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Copy static assets
    import shutil
    if os.path.exists('flask_portfolio/static'):
        shutil.copytree('flask_portfolio/static', os.path.join(output_dir, 'static'))
    
    # Copy version.json for reference
    if os.path.exists('version.json'):
        shutil.copy2('version.json', output_dir)
    
    with app.app_context():
        # Generate index page
        print("📄 Generating index.html...")
        with app.test_client() as client:
            response = client.get('/')
            if response.status_code == 200:
                with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
                    # Fix relative URLs for static hosting
                    content = response.get_data(as_text=True)
                    # Replace Flask url_for calls with relative paths
                    content = content.replace('href="/static/', 'href="static/')
                    content = content.replace('src="/static/', 'src="static/')
                    f.write(content)
                print("✅ index.html generated")
            else:
                print(f"❌ Error generating index: {response.status_code}")
        
        # Generate tutorials pages
        print("📚 Generating tutorials pages...")
        os.makedirs(os.path.join(output_dir, 'tutorials'), exist_ok=True)
        
        # Tutorials list page
        with app.test_client() as client:
            response = client.get('/tutorials/')
            if response.status_code == 200:
                with open(os.path.join(output_dir, 'tutorials.html'), 'w', encoding='utf-8') as f:
                    content = response.get_data(as_text=True)
                    content = content.replace('href="/static/', 'href="static/')
                    content = content.replace('src="/static/', 'src="static/')
                    content = content.replace('href="/tutorials/', 'href="tutorials/')
                    f.write(content)
                print("✅ tutorials.html generated")
        
        # Individual tutorial pages
        for tutorial in tutorials:
            with app.test_client() as client:
                response = client.get(f'/tutorials/{tutorial.slug}/')
                if response.status_code == 200:
                    filename = f'{tutorial.slug}.html'
                    with open(os.path.join(output_dir, 'tutorials', filename), 'w', encoding='utf-8') as f:
                        content = response.get_data(as_text=True)
                        content = content.replace('href="/static/', 'href="../static/')
                        content = content.replace('src="/static/', 'src="../static/')
                        content = content.replace('href="/tutorials/', 'href="../tutorials/')
                        f.write(content)
                    print(f"✅ tutorials/{filename} generated")
        
        # Generate projects pages
        print("🚀 Generating projects pages...")
        os.makedirs(os.path.join(output_dir, 'projects'), exist_ok=True)
        
        # Projects list page
        with app.test_client() as client:
            response = client.get('/projects/')
            if response.status_code == 200:
                with open(os.path.join(output_dir, 'projects.html'), 'w', encoding='utf-8') as f:
                    content = response.get_data(as_text=True)
                    content = content.replace('href="/static/', 'href="static/')
                    content = content.replace('src="/static/', 'src="static/')
                    content = content.replace('href="/projects/', 'href="projects/')
                    f.write(content)
                print("✅ projects.html generated")
        
        # Individual project pages
        for project in projects:
            with app.test_client() as client:
                response = client.get(f'/projects/{project.slug}/')
                if response.status_code == 200:
                    filename = f'{project.slug}.html'
                    with open(os.path.join(output_dir, 'projects', filename), 'w', encoding='utf-8') as f:
                        content = response.get_data(as_text=True)
                        content = content.replace('href="/static/', 'href="../static/')
                        content = content.replace('src="/static/', 'src="../static/')
                        content = content.replace('href="/projects/', 'href="../projects/')
                        f.write(content)
                    print(f"✅ projects/{filename} generated")
    
    # Create a simple .htaccess for better routing
    htaccess_content = """
# Static site routing
DirectoryIndex index.html

# Handle missing extensions
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([^.]+)$ $1.html [NC,L]

# Cache static assets
<FilesMatch "\.(css|js|png|jpg|jpeg|gif|svg|ico)$">
    ExpiresActive on
    ExpiresDefault "access plus 1 month"
</FilesMatch>

# Security headers
Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options DENY
Header always set X-XSS-Protection "1; mode=block"
"""
    
    with open(os.path.join(output_dir, '.htaccess'), 'w') as f:
        f.write(htaccess_content)
    
    print(f"\n✅ Static site generated successfully in '{output_dir}' directory!")
    print("\n📁 Generated files:")
    for root, dirs, files in os.walk(output_dir):
        level = root.replace(output_dir, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

if __name__ == '__main__':
    print("🏗️ Generating static site from Flask application...")
    print("=" * 50)
    generate_static_site()
