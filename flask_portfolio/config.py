import os

class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback-dev-key-change-immediately'
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    HOST = os.environ.get('FLASK_HOST', '127.0.0.1')
    PORT = int(os.environ.get('FLASK_PORT', 5001))
    
    # Security settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Must be set in production
    
    # Enhanced security for production
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
    SESSION_COOKIE_SECURE = True

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SESSION_COOKIE_SECURE = False  # Allow HTTP in development

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'testing-key-not-for-production'
    SESSION_COOKIE_SECURE = False

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
