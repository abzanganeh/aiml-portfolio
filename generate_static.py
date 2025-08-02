#!/usr/bin/env python3
"""
Static Site Generator for Flask Portfolio
Converts Flask templates to static HTML files for shared hosting deployment
"""

import os
import sys
from flask import Flask
sys.path.append('flask_portfolio')

def generate_static_site():
    """Generate static HTML files from Flask application"""
    
    # Import Flask app
    from app import app
    from models.tutorial import Tutorial
    from models.project import Project
    
    # Create output directory
    output_dir = 'static_site'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Copy static assets
    import shutil
    static_src = 'flask_portfolio/static'
    static_dest = os.path.join(output_dir, 'static')
    if os.path.exists(static_dest):
        shutil.rmtree(static_dest)
    shutil.copytree(static_src, static_dest)
    
    print("📁 Static assets copied")
    
    with app.test_client() as client:
        # Generate main pages
        pages = [
            ('/', 'index.html'),
            ('/tutorials', 'tutorials.html'),
            ('/projects', 'projects.html'),
        ]
        
        # Generate tutorial pages
        tutorials = Tutorial.get_all()
        for tutorial in tutorials:
            pages.append((f'/tutorials/{tutorial.slug}', f'tutorials/{tutorial.slug}.html'))
        
        # Generate project pages  
        projects = Project.get_all()
        for project in projects:
            pages.append((f'/projects/{project.slug}', f'projects/{project.slug}.html'))
        
        # Generate all pages
        for route, filename in pages:
            try:
                print(f"🔄 Generating {filename} from {route}")
                
                # Create directory if needed
                file_dir = os.path.join(output_dir, os.path.dirname(filename))
                if file_dir and not os.path.exists(file_dir):
                    os.makedirs(file_dir)
                
                # Get page content
                response = client.get(route)
                if response.status_code == 200:
                    # Fix relative paths for static files
                    content = response.get_data(as_text=True)
                    
                    # Adjust CSS and JS paths based on depth
                    depth = filename.count('/')
                    if depth > 0:
                        prefix = '../' * depth
                        content = content.replace('href="static/', f'href="{prefix}static/')
                        content = content.replace('src="static/', f'src="{prefix}static/')
                        # Fix Flask url_for calls to static paths
                        content = content.replace("url_for('static', filename='css/main.css')", f"'{prefix}static/css/main.css'")
                        content = content.replace("url_for('static', filename='js/main.js')", f"'{prefix}static/js/main.js'")
                        # Fix navigation links
                        content = content.replace("url_for('home')", "'/' if depth == 0 else '../index.html'")
                        content = content.replace("url_for('tutorials_list')", f"'{'../' * depth}tutorials.html'")
                        content = content.replace("url_for('projects_list')", f"'{'../' * depth}projects.html'")
                    else:
                        # Fix Flask url_for calls for root level files
                        content = content.replace("url_for('static', filename='css/main.css')", "'static/css/main.css'")
                        content = content.replace("url_for('static', filename='js/main.js')", "'static/js/main.js'")
                        content = content.replace("url_for('home')", "'index.html'")
                        content = content.replace("url_for('tutorials_list')", "'tutorials.html'")
                        content = content.replace("url_for('projects_list')", "'projects.html'")
                    
                    # Fix remaining Flask template calls
                    import re
                    content = re.sub(r"url_for\('([^']+)',\s*slug='([^']+)'\)", r'\1/\2.html', content)
                    content = re.sub(r"url_for\('([^']+)'\)", r'\1.html', content)
                    
                    # Write file
                    filepath = os.path.join(output_dir, filename)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"✅ Generated {filename}")
                else:
                    print(f"❌ Failed to generate {filename} (status: {response.status_code})")
                    
            except Exception as e:
                print(f"❌ Error generating {filename}: {str(e)}")
    
    print(f"\n🎉 Static site generated in '{output_dir}' directory")
    print(f"📊 Generated {len([f for f in os.listdir(output_dir) if f.endswith('.html')])} HTML files")

if __name__ == '__main__':
    generate_static_site()
