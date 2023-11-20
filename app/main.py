import uvicorn

from datetime import datetime

from fastapi import FastAPI, HTTPException

from app.db import SessionLocal, TextTable
from app.dto import TextCreate
from app.queue import sent_to_rabbit
from app.queue import count_x

# Создаем экземпляр FastAPI
app = FastAPI()


# Ручка для сохранения текста в базе данных
@app.post("/create-text/")
async def create_text(info: TextCreate):
    sent_to_rabbit(info.text)
    db = SessionLocal()
    db_text = TextTable(datetime=datetime.now(), title=info.title, x_avg_count_in_line=count_x(info.text))
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    db.close()
    return 'Message send!'


# Ручка для получения текста из базы данных
@app.get("/get-text/")
async def get_text():
    db = SessionLocal()
    db_text = db.query(TextTable).all()
    db.close()
    if db_text is None:
        raise HTTPException(status_code=404, detail="Text not found")
    return db_text


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8888)
