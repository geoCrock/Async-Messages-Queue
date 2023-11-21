import asyncio

import uvicorn

from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from typing import List


from app.db import SessionLocal, TextTable
from app.dto import TextCreate
from app.async_queue import send_message, receive_message


# Используем контекстный менеждер ака новый startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    await receive_message()
    yield

# Создаем экземпляр FastAPI
app = FastAPI(lifespan=lifespan)


# Ручка для сохранения текста в базе данных
@app.post("/count-x-from-text/")
async def count_x_from_text(info: List[TextCreate]):
    for i in info:
        datetime = i.datetime
        title = i.title
        text = i.text
        await send_message(datetime, title, text)
    # Интервал 3 секунды
    await asyncio.sleep(3)
    return 'Messages send!'


# Ручка для получения текста из базы данных
@app.get("/get-x/")
async def get_x():
    db = SessionLocal()
    db_text = (db.query(TextTable.datetime, TextTable.title, TextTable.x_avg_count_in_line)
               .order_by(TextTable.id.desc()).all())
    db.close()
    if db_text is None:
        raise HTTPException(status_code=404, detail="Text not found")
    return db_text


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8888)
