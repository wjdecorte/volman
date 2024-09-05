
# Volman - Volunteer Management Application

To start the Postgres database:

    docker-compose up -d postgres

To start the Connectors service:

    docker-compose up api

To add or remove dependencies:
    NOTE: Be sure poetry has been installed on your machine.  On Mac, use `brew install poetry`.

    poetry add <package_name>@~<x.x>
    poetry add requests@~2.24

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

### Docker Compose Commands
NOTE: All commands are executed from project root directory.

    COMPOSE_DOCKER_CLI_BUILD=1 docker-compose up [--build]

### Docker Build Commands
NOTE: All commands should be executed from project root directory.

    docker build -t volman .

## Branch Management

When starting any new development, branch from `dev` and open your pull requests
against `dev`. Try to avoid working in a long-lived feature branch. Small,
self-contained commits and pull requests make this easier. Sometimes you'll need
to set a configuration or feature flag to prevent incomplete features from being
included in code paths.


The `master` branch must be deploy-able at any time, which means that:
- We need to be reasonably sure that the merge is bug-free.
- Data layer changes should be forwards and backwards compatible.
- Any new operational dependencies should be met before merging.


# Deployment

- git checkout dev
- git pull --rebase
- git checkout -b <new_branch>
- git push --set-upstream origin <new_branch>
- Merge <new_branch> to dev using PR
- git checkout dev
- git pull --rebase
- Merge master into dev via PR (Only if dev was previously merged into master)
- git pull --rebase (dev branch)
- Merge dev into master via PR
