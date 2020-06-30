import os
from os.path import dirname, abspath


class Config:
    HOST = '0.0.0.0'
    PORT = 5000
    SECRET_KEY = ''

    DEBUG = False

    APP_DIR = os.path.abspath(os.path.realpath(__file__))
    PROJECT_FOLDER_DIRECTORY = str.replace(dirname(abspath(__file__)), "\\", "/")
    ROOT_DIRECTORY = str.replace(dirname(dirname(abspath(__file__))), "\\", "/")

    REST_URL_PREFIX = '/api/'

    DATABASE_CONFIGURATION = {
        "user": 'root',
        "password": '',
        "host": 'localhost',
        "database": '',
    }

    def __init__(self, app):
        pass

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    API_KEY = ''
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    API_KEY = ''
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = True


class ProductionConfig(Config):
    API_KEY = ''
    DEBUG = False
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
