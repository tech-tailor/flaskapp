# application factory for the flask app

import os
from flask import Flask

def create_app(test_config=None):
    """
    create and configure the app
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    @app.route('/')
    def hi():
        return 'Hello'
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)


    return app