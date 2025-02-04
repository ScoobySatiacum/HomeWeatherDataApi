import os
import logging

from flask import Flask

logger = logging.getLogger(__name__)

def create_app(test_config=None):
    logging.basicConfig(filename="", level=logging.INFO, format='%(asctime)s %(message)s')

    logger.info("Home Weather Data API starting.")

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='/srv/weather_data_api/weather_data.sqlite',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    logger.info("Registering API blueprint")

    with app.app_context():
        from . import api
        app.register_blueprint(api.bp)
        app.add_url_rule('/', endpoint='index')

    logger.info("API started.")

    return app