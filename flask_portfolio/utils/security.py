"""
Security utilities for the Flask portfolio application
"""

from flask import request, jsonify
import html
import re
from typing import Dict, Tuple, Any
import logging

logger = logging.getLogger(__name__)

def add_security_headers(response):
    """Add security headers to all responses"""
    # Prevent MIME type sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # Prevent clickjacking
    response.headers['X-Frame-Options'] = 'DENY'
    
    # XSS protection
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # HTTPS enforcement (if using HTTPS)
    if request.is_secure:
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    
    # Content Security Policy
    csp = (
        "default-src 'self'; "
        "style-src 'self' 'unsafe-inline' cdnjs.cloudflare.com fonts.googleapis.com; "
        "script-src 'self' cdnjs.cloudflare.com; "
        "font-src 'self' cdnjs.cloudflare.com fonts.gstatic.com; "
        "img-src 'self' data: https:; "
        "connect-src 'self'"
    )
    response.headers['Content-Security-Policy'] = csp
    
    return response

def sanitize_input(input_data: str) -> str:
    """Sanitize user input to prevent XSS"""
    if not isinstance(input_data, str):
        input_data = str(input_data)
    
    # HTML escape the input
    sanitized = html.escape(input_data.strip())
    
    # Additional sanitization for common attack vectors
    sanitized = re.sub(r'[<>"\']', '', sanitized)
    
    return sanitized

def validate_prediction_input(data: Dict[str, Any]) -> Tuple[bool, str, Dict[str, Any]]:
    """
    Validate and sanitize ML model prediction inputs
    
    Returns:
        Tuple of (is_valid, error_message, sanitized_data)
    """
    required_fields = {
        'pclass': {'type': int, 'min': 1, 'max': 3},
        'sex': {'type': str, 'values': ['male', 'female']},
        'age': {'type': float, 'min': 0, 'max': 120},
        'sibsp': {'type': int, 'min': 0, 'max': 10},
        'parch': {'type': int, 'min': 0, 'max': 10},
        'fare': {'type': float, 'min': 0, 'max': 1000},
        'embarked': {'type': str, 'values': ['C', 'Q', 'S']},
        'title': {'type': str, 'values': ['Mr', 'Mrs', 'Miss', 'Master', 'Dr', 'Rev', 'Other']}
    }
    
    sanitized_data = {}
    
    # Check for required fields
    for field, rules in required_fields.items():
        if field not in data:
            return False, f"Missing required field: {field}", {}
        
        value = data[field]
        
        try:
            # Type conversion and validation
            if rules['type'] == int:
                value = int(value)
                if 'min' in rules and value < rules['min']:
                    return False, f"Invalid {field}: too small", {}
                if 'max' in rules and value > rules['max']:
                    return False, f"Invalid {field}: too large", {}
                    
            elif rules['type'] == float:
                value = float(value)
                if 'min' in rules and value < rules['min']:
                    return False, f"Invalid {field}: too small", {}
                if 'max' in rules and value > rules['max']:
                    return False, f"Invalid {field}: too large", {}
                    
            elif rules['type'] == str:
                value = sanitize_input(str(value))
                if 'values' in rules and value not in rules['values']:
                    return False, f"Invalid {field}: not in allowed values", {}
            
            sanitized_data[field] = value
            
        except (ValueError, TypeError) as e:
            logger.warning(f"Input validation error for field {field}: {e}")
            return False, f"Invalid {field}: invalid format", {}
    
    return True, "Valid", sanitized_data

def log_security_event(event_type: str, details: str, request_info: Dict[str, Any] = None):
    """Log security-related events"""
    if request_info is None:
        request_info = {
            'ip': request.remote_addr,
            'user_agent': request.headers.get('User-Agent', ''),
            'endpoint': request.endpoint,
            'method': request.method
        }
    
    logger.warning(f"SECURITY_EVENT: {event_type} - {details} - {request_info}")

def validate_slug(slug: str) -> bool:
    """Validate URL slug format"""
    if not slug or not isinstance(slug, str):
        return False
    
    # Allow only lowercase letters, numbers, and hyphens
    pattern = r'^[a-z0-9-]+$'
    return bool(re.match(pattern, slug)) and len(slug) <= 100
