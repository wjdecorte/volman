from functools import lru_cache

from flask import Flask
from flask_alembic import Alembic

from volman import Settings
from volman.models.tables import db


@lru_cache
def get_settings():
    return Settings()


def create_app():
    app = Flask("volman")

    settings = get_settings()

    app.config.update(
        SQLALCHEMY_DATABASE_URI=f"postgresql+psycopg2://{settings.database_user}:{settings.database_pswd}@{settings.database_host}:{settings.database_port}/{settings.database_name}"
    )
    app.config.update(SQLALCHEMY_TRACK_MODIFICATIONS=False)
    # app.config.update(SQLALCHEMY_ECHO=service_config.debug_mode is True)  # Extreme debug only
    app.config.update(SQLALCHEMY_ENGINE_OPTIONS={"pool_pre_ping": True})
    app.config["ALEMBIC"] = dict(script_location="migrations")

    db.init_app(app)

    # Apply database migrations
    alembic = Alembic()
    alembic.init_app(app, run_mkdir=False)
    with app.app_context():
        # alembic.downgrade()
        alembic.revision("Base Tables")
        # alembic.upgrade()

    return app
