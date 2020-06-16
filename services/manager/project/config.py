import os


class BaseConfig:
    """Base Configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing Configuration"""
    DEBUG_TB_ENABLED = True
