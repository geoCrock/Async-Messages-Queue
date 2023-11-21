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
@app.post("/add-text/")
async def add_text(info: List[TextCreate]):
    print(info)
    for item in info:
        title = item.title
        text = item.text
        await send_message(title, text)
    # Интервал 3 секунды
    await asyncio.sleep(3)
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
