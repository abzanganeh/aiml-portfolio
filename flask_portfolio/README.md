# Flask Portfolio

Modern, object-oriented Flask web application for showcasing machine learning expertise.

## Features

- **Object-Oriented Architecture**: Clean Python classes for tutorials and projects
- **Responsive Design**: Modern UI with ML/AI focused styling
- **Interactive Content**: Filterable tutorials and projects
- **Professional Layout**: Clean separation of content and presentation
- **Educational Focus**: Comprehensive learning resources

## Structure

```
flask_portfolio/
├── app.py                  # Main Flask application
├── models/                 # Python data models
│   ├── tutorial.py         # Tutorial class
│   └── project.py          # Project class
├── templates/              # Jinja2 templates
│   ├── base.html           # Base template
│   ├── index.html          # Homepage
│   ├── tutorials.html      # Tutorial listing
│   ├── projects.html       # Project listing
│   └── tutorial_detail.html # Tutorial detail template
├── static/                 # Static assets
│   ├── css/main.css        # Main stylesheet
│   └── js/main.js          # JavaScript functionality
└── requirements.txt        # Python dependencies
```

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the development server:
   ```bash
   python app.py
   ```

3. Access the application:
   ```
   http://localhost:5001
   ```

## Conversion Status

- ✅ Flask application structure
- ✅ Object-oriented models
- ✅ Modern responsive design
- ✅ Tutorial conversion (Naive Bayes, Linear Regression)
- 🔄 Remaining tutorial conversions
- 🔄 Project detail pages
- 🔄 Interactive features

## Technology Stack

- **Backend**: Flask, Python 3.x
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with CSS Variables
- **Architecture**: MVC pattern with class-based models
