import database
import sqlalchemy as sa
from config import settings

database = database.Database(settings.database_url)
metadata = sa.MetaData()

if settings.environment == "production":
    engine = sa.create_engine(settings.database_url)
else:
    engine = sa.create_engine(settings.database_url, connect_args={"check_same_thread": False})