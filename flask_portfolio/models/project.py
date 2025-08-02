import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class Project:
    """Project model for machine learning portfolio projects"""
    
    def __init__(self, title: str, slug: str, description: str, tech_stack: List[str],
                 status: str, demo_url: str = None, github_url: str = None,
                 features: List[str] = None, created_date: str = None):
        self.title = title
        self.slug = slug
        self.description = description
        self.tech_stack = tech_stack
        self.status = status  # active, development, planning
        self.demo_url = demo_url
        self.github_url = github_url
        self.features = features or []
        self.created_date = created_date or datetime.now().isoformat()
    
    @classmethod
    def get_all(cls) -> List['Project']:
        """Get all projects from data"""
        projects = []
        
        # Titanic Survival Prediction
        projects.append(cls(
            title="Titanic Survival Prediction",
            slug="titanic-survival",
            description="Machine learning classification model predicting passenger survival using historical Titanic data",
            tech_stack=["Python", "Pandas", "Scikit-learn", "Matplotlib"],
            status="active",
            demo_url="/projects/titanic-survival-prediction/",
            features=[
                "Data preprocessing and feature engineering",
                "Multiple classification algorithms comparison", 
                "Interactive prediction interface",
                "Model performance visualization"
            ]
        ))
        
        # LLM Applications
        projects.append(cls(
            title="Large Language Model Applications",
            slug="llm-applications",
            description="Exploring practical applications of large language models in various domains",
            tech_stack=["Python", "Transformers", "OpenAI API", "Streamlit"],
            status="development",
            features=[
                "Text generation and completion",
                "Question answering systems",
                "Document summarization",
                "Code generation assistance"
            ]
        ))
        
        # Neural Networks Project
        projects.append(cls(
            title="Deep Neural Networks",
            slug="neural-networks-project",
            description="Implementation of various neural network architectures for different machine learning tasks",
            tech_stack=["Python", "TensorFlow", "Keras", "NumPy"],
            status="development",
            features=[
                "Convolutional Neural Networks",
                "Recurrent Neural Networks", 
                "Custom layer implementations",
                "Transfer learning examples"
            ]
        ))
        
        # AI Innovation
        projects.append(cls(
            title="AI Innovation Lab",
            slug="ai-innovation",
            description="Experimental AI solutions and cutting-edge machine learning research implementations",
            tech_stack=["Python", "PyTorch", "Research Papers", "Jupyter"],
            status="planning",
            features=[
                "Research paper implementations",
                "Novel algorithm development",
                "Experimental model architectures",
                "Performance benchmarking"
            ]
        ))
        
        # ML Pipeline
        projects.append(cls(
            title="ML Pipeline Framework",
            slug="ml-pipeline",
            description="End-to-end machine learning pipeline for data processing, training, and deployment",
            tech_stack=["Python", "MLflow", "Docker", "FastAPI"],
            status="development",
            features=[
                "Automated data preprocessing",
                "Model training orchestration",
                "Experiment tracking",
                "Production deployment"
            ]
        ))
        
        # Statistical Analysis
        projects.append(cls(
            title="Advanced Statistical Analysis",
            slug="statistical-analysis", 
            description="Comprehensive statistical analysis tools and visualization for data science workflows",
            tech_stack=["Python", "SciPy", "Statsmodels", "Plotly"],
            status="planning",
            features=[
                "Hypothesis testing frameworks",
                "Advanced statistical modeling",
                "Interactive data visualization",
                "Automated report generation"
            ]
        ))
        
        return projects
    
    @classmethod
    def get_by_slug(cls, slug: str) -> Optional['Project']:
        """Get project by slug"""
        projects = cls.get_all()
        for project in projects:
            if project.slug == slug:
                return project
        return None
    
    @classmethod
    def get_by_status(cls, status: str) -> List['Project']:
        """Get projects by status"""
        projects = cls.get_all()
        return [p for p in projects if p.status == status]
    
    def to_dict(self) -> Dict:
        """Convert project to dictionary"""
        return {
            'title': self.title,
            'slug': self.slug,
            'description': self.description,
            'tech_stack': self.tech_stack,
            'status': self.status,
            'demo_url': self.demo_url,
            'github_url': self.github_url,
            'features': self.features,
            'created_date': self.created_date
        }
    
    def get_status_badge_class(self) -> str:
        """Get CSS class for status badge"""
        status_classes = {
            'active': 'badge-success',
            'development': 'badge-warning',
            'planning': 'badge-secondary'
        }
        return status_classes.get(self.status, 'badge-secondary')
    
    def get_status_display(self) -> str:
        """Get display text for status"""
        status_display = {
            'active': 'Live Demo',
            'development': 'In Development', 
            'planning': 'Coming Soon'
        }
        return status_display.get(self.status, 'Unknown')
