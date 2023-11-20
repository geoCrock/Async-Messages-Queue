from databases import Database
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import POSTGRESQL_URL

# Подключаемся к базе данных
DATABASE_URL = POSTGRESQL_URL
database = Database(DATABASE_URL)
metadata = declarative_base()


# Определяем модель для таблицы в базе данных
class TextTable(metadata):
    __tablename__ = "texts5"
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(String)
    title = Column(String)
    x_avg_count_in_line = Column(Float)


# Создаем таблицу в базе данных
engine = create_engine(DATABASE_URL)
metadata.metadata.create_all(bind=engine)

# Создаем сессию для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
