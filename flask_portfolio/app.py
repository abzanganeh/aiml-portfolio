from flask import Flask, render_template, request, jsonify
from models.tutorial import Tutorial
from models.project import Project
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-change-in-production'

@app.route('/')
def home():
    """Main portfolio homepage"""
    tutorials = Tutorial.get_all()
    projects = Project.get_all()
    return render_template('index.html', 
                         tutorials=tutorials, 
                         projects=projects)

@app.route('/tutorials')
def tutorials_list():
    """List all tutorials with filtering"""
    tutorials = Tutorial.get_all()
    tags = Tutorial.get_all_tags()
    return render_template('tutorials.html', 
                         tutorials=tutorials, 
                         tags=tags)

@app.route('/tutorials/<slug>')
def tutorial_detail(slug):
    """Individual tutorial page"""
    tutorial = Tutorial.get_by_slug(slug)
    if not tutorial:
        return render_template('404.html'), 404
    
    # Route to specific tutorial template if it exists
    template_name = f'{slug.replace("-", "_")}_detail.html'
    try:
        return render_template(template_name, tutorial=tutorial)
    except:
        # Fall back to generic template
        return render_template('tutorial_detail.html', tutorial=tutorial)

@app.route('/projects')
def projects_list():
    """List all projects"""
    projects = Project.get_all()
    return render_template('projects.html', projects=projects)

@app.route('/projects/<slug>')
def project_detail(slug):
    """Individual project page"""
    project = Project.get_by_slug(slug)
    if not project:
        return render_template('404.html'), 404
    
    # Route to specific project template if it exists
    template_name = f'{slug.replace("-", "_")}_detail.html'
    try:
        return render_template(template_name, project=project)
    except:
        # Fall back to generic template
        return render_template('project_detail.html', project=project)

@app.route('/api/tutorials')
def api_tutorials():
    """API endpoint for tutorials"""
    tutorials = Tutorial.get_all()
    return jsonify([t.to_dict() for t in tutorials])

@app.route('/api/projects')
def api_projects():
    """API endpoint for projects"""
    projects = Project.get_all()
    return jsonify([p.to_dict() for p in projects])

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
