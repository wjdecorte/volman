
# Volman - Volunteer Management Application

Sample code for the suggested database schema for the application.  Contains SQLAlchemy models defining the tables, columns and relationships.


### Docker Build Commands
NOTE: All commands should be executed from project root directory.

    docker build -t volman .

### Running the services
To start the Postgres database separately as a background process:

    docker compose up -d postgres

To initialize or upgrade the database:

    docker compose up db-init

To start the PGAdmin app (use the '-d' flag to run in background):

    docker compose up pgadmin 

### Database Migrations
To Create a new revision using Flask-Alembic:

Set the environment variable REVISION_MSG with an short message about the revision and then run db-rev service.

    REVISION_MSG="<enter message here>" docker compose up db-rev 

NOTE: Be sure Postgres is running!

After generating the migration script, review and adjust as needed.  Update `down_revision` if not properly updated.

### Dependency Management

To add or remove dependencies:
    NOTE: Be sure poetry has been installed on your machine.  On Mac, use `brew install poetry`.

    poetry add <package_name>
    poetry add requests

    poetry remove <package_name>
    poetry remove requests

    poetry install
