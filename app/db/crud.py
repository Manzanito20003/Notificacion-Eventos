# CRUD operations placeholder
from app.db.database import engine, metadata
from app.db.models import pages

metadata.create_all(engine)

# Example: functions to interact with DB will go here
