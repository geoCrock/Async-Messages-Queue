import uvicorn

from datetime import datetime

from fastapi import FastAPI, HTTPException

from app.db import SessionLocal, TextTable
from app.dto import TextCreate
from app.queue import send_to_rabbit

# Создаем экземпляр FastAPI
app = FastAPI()


# Ручка для сохранения текста в базе данных
@app.post("/create-text/")
async def create_text(info: TextCreate):
    send_to_rabbit(info.text)
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
