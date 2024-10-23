# Backend

Common Commands
Here are the most common Flask-Migrate commands:

flask db init: Initialize the migration repository.
flask db migrate -m "Message": Generate a migration based on model changes.
flask db upgrade: Apply the migration to the database.
flask db downgrade: Revert the most recent migration.
flask db history: Show a list of all migrations.
flask db current: Show the current migration applied.