from 
from flask import Flask
from flask_alembic import Alembic

from volman import Settings

@lru_cache
def get_settings():
    return Settings()

def create_app():
    app = Flask("volman")

    app.config.update(
        SQLALCHEMY_DATABASE_URI=f"postgresql+psycopg2://{user}:{pswd}@{host}:{port}/{name}"
    )
    app.config.update(SQLALCHEMY_TRACK_MODIFICATIONS=False)
    # app.config.update(SQLALCHEMY_ECHO=service_config.debug_mode is True)  # Extreme debug only
    app.config.update(SQLALCHEMY_ENGINE_OPTIONS={"pool_pre_ping": True})
    app.config["ALEMBIC"] = dict(script_location="connectors/migrations")

    db.init_app(app)

    # Add error handler
    app.register_error_handler(Exception, handle_exception)

    # Apply database migrations
    app.logger.info("Update database tables")
    alembic = Alembic()
    alembic.init_app(app, run_mkdir=False)
    with app.app_context():
        # alembic.downgrade()
        # alembic.revision("enter Message here")
        alembic.upgrade()

    api.register_blueprint(common.api, url_prefix=service_config.base_url_prefix)
    api.register_blueprint(
        file_connectors.api, url_prefix=f"{service_config.base_url_prefix}/file"
    )
    api.register_blueprint(
        api_connectors.api, url_prefix=f"{service_config.base_url_prefix}/api-conn"
    )

    api.register_blueprint(
        api_token_gen.api, url_prefix=f"{service_config.base_url_prefix}/access"
    )

    # Add response logging
    app.after_request(after_request)

    # Add tracing
    FlaskInstrumentor().instrument_app(app, excluded_urls=".*/healthcheck")
    RequestsInstrumentor().instrument()
    return app
