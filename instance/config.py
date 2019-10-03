import os

class Config(object):
    """
    parent config class
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

class DevelopmentConfig(Config):
    """
    Development configuration
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Testing configuration with a separate DATABASE
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "b_name='scaling-waffle' host='localhost' port='5432' user='postgres' password='toor'"
    DEBUG = True

class StagingConfig(Config):
    """
    configuration for staging
    """
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
