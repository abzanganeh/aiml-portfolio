from flask import Flask, render_template, request, jsonify
from models.tutorial import Tutorial
from models.project import Project
from utils.security import add_security_headers, validate_prediction_input, log_security_event, validate_slug
from config import config
import os
import logging
import json
from datetime import datetime

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not available, use system environment variables

# Load version information
def get_version_info():
    version_file = os.path.join(os.path.dirname(__file__), '..', 'version.json')
    try:
        with open(version_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "version": "2.0.0",
            "build_id": "20250803-0000",
            "build_date": "2025-08-03",
            "description": "Second website iteration with comprehensive features"
        }

# Create Flask app with environment-based configuration
config_name = os.environ.get('FLASK_CONFIG', 'development')
app = Flask(__name__)
app.config.from_object(config[config_name])

# Context processor to inject global variables
@app.context_processor
def inject_globals():
    return {
        'current_year': datetime.now().year,
        'version_info': get_version_info(),
        'moment': datetime
    }

# Configure logging
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    file_handler = logging.FileHandler('logs/portfolio.log')
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Portfolio application startup')

# Add security headers to all responses
app.after_request(add_security_headers)

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
    # Validate slug for security
    if not validate_slug(slug):
        log_security_event("INVALID_SLUG", f"Invalid tutorial slug: {slug}")
        return render_template('404.html'), 404
    
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
    # Validate slug for security
    if not validate_slug(slug):
        log_security_event("INVALID_SLUG", f"Invalid project slug: {slug}")
        return render_template('404.html'), 404
    
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
    """Handle 404 errors"""
    app.logger.info(f'404 error: {request.url}')
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    app.logger.error(f'Server Error: {error}')
    return render_template('error.html', 
                         error="An internal server error occurred" if not app.debug else str(error)), 500

if __name__ == '__main__':
    # Use environment variables for host and port
    host = app.config.get('HOST', '127.0.0.1')
    port = app.config.get('PORT', 5001)
    debug = app.config.get('DEBUG', False)
    
    app.run(debug=debug, host=host, port=port)
