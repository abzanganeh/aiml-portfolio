import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class Tutorial:
    """Tutorial model for machine learning guides"""
    
    def __init__(self, title: str, slug: str, description: str, content: str, 
                 tags: List[str], difficulty: str, read_time: int, 
                 created_date: str = None):
        self.title = title
        self.slug = slug
        self.description = description
        self.content = content
        self.tags = tags
        self.difficulty = difficulty  # beginner, intermediate, advanced
        self.read_time = read_time  # minutes
        self.created_date = created_date or datetime.now().isoformat()
    
    @classmethod
    def get_all(cls) -> List['Tutorial']:
        """Get all tutorials from data"""
        tutorials = []
        
        # Naive Bayes
        tutorials.append(cls(
            title="Naive Bayes Classification",
            slug="naive-bayes",
            description="Probabilistic classification algorithm based on Bayes theorem",
            content="", # Will be loaded from template
            tags=["classification", "probability", "beginner"],
            difficulty="beginner",
            read_time=15
        ))
        
        # Decision Trees
        tutorials.append(cls(
            title="Decision Trees",
            slug="decision-trees", 
            description="Tree-based learning algorithm for classification and regression",
            content="",
            tags=["classification", "regression", "interpretable", "beginner"],
            difficulty="beginner",
            read_time=20
        ))
        
        # Neural Networks
        tutorials.append(cls(
            title="Neural Networks",
            slug="neural-networks",
            description="Deep learning fundamentals and neural network architectures",
            content="",
            tags=["deep-learning", "neural-networks", "intermediate"],
            difficulty="intermediate", 
            read_time=30
        ))
        
        # Linear Regression
        tutorials.append(cls(
            title="Linear Regression",
            slug="linear-regression",
            description="Statistical regression analysis and predictive modeling",
            content="",
            tags=["regression", "statistics", "beginner"],
            difficulty="beginner",
            read_time=18
        ))
        
        # Clustering
        tutorials.append(cls(
            title="Clustering Algorithms",
            slug="clustering",
            description="Unsupervised learning techniques for data grouping",
            content="",
            tags=["clustering", "unsupervised", "intermediate"],
            difficulty="intermediate",
            read_time=25
        ))
        
        # Feature Engineering
        tutorials.append(cls(
            title="Feature Engineering",
            slug="feature-engineering",
            description="Data preprocessing and feature selection techniques",
            content="",
            tags=["preprocessing", "feature-selection", "intermediate"],
            difficulty="intermediate",
            read_time=22
        ))
        
        return tutorials
    
    @classmethod
    def get_by_slug(cls, slug: str) -> Optional['Tutorial']:
        """Get tutorial by slug"""
        tutorials = cls.get_all()
        for tutorial in tutorials:
            if tutorial.slug == slug:
                return tutorial
        return None
    
    @classmethod
    def get_all_tags(cls) -> List[str]:
        """Get all unique tags"""
        tutorials = cls.get_all()
        tags = set()
        for tutorial in tutorials:
            tags.update(tutorial.tags)
        return sorted(list(tags))
    
    def to_dict(self) -> Dict:
        """Convert tutorial to dictionary"""
        return {
            'title': self.title,
            'slug': self.slug,
            'description': self.description,
            'tags': self.tags,
            'difficulty': self.difficulty,
            'read_time': self.read_time,
            'created_date': self.created_date
        }
    
    def get_difficulty_badge_class(self) -> str:
        """Get CSS class for difficulty badge"""
        difficulty_classes = {
            'beginner': 'badge-success',
            'intermediate': 'badge-warning', 
            'advanced': 'badge-danger'
        }
        return difficulty_classes.get(self.difficulty, 'badge-secondary')
