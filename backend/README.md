
# Backend
De backend regelt de data voor de frontend. Het maakt een connectie met de PostgreSQL database waar informatie is opgeslagen zoals de gebruikers, de verzekeringen en welke auto's er verzekerd zijn. 
### Car endpoints
- **GET /cars/**: haal alle auto's op
- **POST /cars/**: voeg een nieuwe auto toe aan de collectie
- **GET /cars/id/**: haal 1 auto op
- **GET /customer/cars/username/**: haal alle auto's van een specifieke gebruiker op
- **DELETE /cars/licenceplate/**: verwijder een auto

### Customer endpoints
- **GET /customers/**: haal alle klanten op
- **POST /customers/**: voeg een nieuwe klant toe aan de collectie
- **POST /customers/login/**: controleer of een gebruiker bestaat

### Insurance Policies endpoints
- **GET /insurance_policies/**: haal alle polissen op
- **POST /insurance_policies/**: voeg een nieuwe polis toe aan de collectie
- **GET /insurance_policies/id/**: haal 1 polis op
- **GET /insurance_policies/customer/id**: haal alle polissen op van een klant

### Here are the most common Flask-Migrate commands:
- **flask db init**: Initialize the migration repository.
-  **flask db migrate -m "Message"**: Generate a migration based on model changes.
- **flask db upgrade**: Apply the migration to the database.
- **flask db downgrade**: Revert the most recent migration.
- **flask db history**: Show a list of all migrations.
- **flask db current**: Show the current migration applied.