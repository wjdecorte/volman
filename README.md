
# Volman - Volunteer Management Application

To start all the services:

    docker compose up

To start the Postgres database separately as a background process:

    docker compose up -d postgres

To start the app:

    docker compose up app

To start the PGAdmin app:

    docker compose up pgadmin

To add or remove dependencies:
    NOTE: Be sure poetry has been installed on your machine.  On Mac, use `brew install poetry`.

    poetry add <package_name>
    poetry add requests

    poetry remove <package_name>
    poetry remove requests

    poetry install

### Database Migrations

To Create a new revision using Alembic:

Update app.py temporarily by uncommenting `alembic.revision` and commenting `alembic.upgrade`.

Enter message inside the double quotes to give the revision meaning.

    with app.app_context():
        alembic.revision("enter Message here")
        # alembic.upgrade()

NOTE: Be sure Postgres is running!

After generating the migration script, review and adjust as needed.  Update `down_revision` if not properly updated.


### Docker Build Commands
NOTE: All commands should be executed from project root directory.

    docker build -t volman .

