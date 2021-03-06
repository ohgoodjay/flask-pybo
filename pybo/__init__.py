#
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # Blueprint
    from .views import main_view, question_views, answer_views
    app.register_blueprint(main_view.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    # @app.route('/r')
    # def hello():
    #     return 'Hello r!'
    #
    # 한글

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
