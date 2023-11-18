import os
from dotenv import load_dotenv

import uvicorn
from datetime import datetime
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from pydantic import BaseModel

load_dotenv()


# Создаем экземпляр FastAPI
app = FastAPI()

# Подключаемся к базе данных
DATABASE_URL = os.environ.get('POSTGRESQL_URL')
database = Database(DATABASE_URL)
metadata = declarative_base()


# Определяем модель для таблицы в базе данных
class TextTable(metadata):
    __tablename__ = "texts3"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(String)
    title = Column(String)
    text = Column(String)



# Создаем таблицу в базе данных
engine = create_engine(DATABASE_URL)
metadata.metadata.create_all(bind=engine)

# Создаем сессию для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Определяем схему для запроса и ответа
class TextCreate(BaseModel):
    title: str
    text: str


# class TextResponse(BaseModel):
#     id: int
#     created_at: datetime
#     title: str
#     text: str


# Ручка для сохранения текста в базе данных
@app.post("/create-text/")
async def create_text(info: TextCreate):
    db = SessionLocal()
    db_text = TextTable(created_at=datetime.now(), title=info.title, text=info.text)
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    db.close()
    return db_text


# Ручка для получения текста из базы данных
@app.get("/get-text/{text_id}")
async def get_text(text_id: int):
    db = SessionLocal()
    db_text = db.query(TextTable).filter(TextTable.id == text_id).first()
    db.close()
    if db_text is None:
        raise HTTPException(status_code=404, detail="Text not found")
    return db_text

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8888)
