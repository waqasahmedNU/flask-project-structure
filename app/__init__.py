from flask import Flask

from app.configuration import config
from app.database.connection import Connection
from app.routes import api_blueprint


class App:
    def __init__(self, configuration_type):
        self.configuration_type = configuration_type

    def initialize(self):
        app = Flask(__name__)
        app.config.from_object(config[self.configuration_type])
        config[self.configuration_type].init_app(app=app)
        app.register_blueprint(api_blueprint, url_prefix='{prefix}'.format(prefix=app.config['REST_URL_PREFIX']))

        # connection = Connection(app.config['DATABASE_CONFIGURATION'])

        @app.before_request
        def before_request():
            # g.connection = connection.create_connection()
            pass

        @app.after_request
        def after_request(response):
            # if g.connection is not None:
            #     connection.close_connection(g.connection)
            #     return response
            # else:
            #     return make_response(jsonify({'status': -5, 'error': 'database Connection Error'}), 500)
            return response
        return app
