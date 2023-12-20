from databases import Database
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import POSTGRESQL_URL

# Connecting to the database
DATABASE_URL = POSTGRESQL_URL
database = Database(DATABASE_URL)
metadata = declarative_base()


# Defining a model for a table in the database
class TextTable(metadata):
    __tablename__ = "x_count_form_text"
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(String)
    title = Column(String)
    x_avg_count_in_line = Column(Float)


# Create a table in the database
engine = create_engine(DATABASE_URL)
metadata.metadata.create_all(bind=engine)

# Create a session to work with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
