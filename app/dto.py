from pydantic import BaseModel


# Определяем схему для запроса и ответа
class TextCreate(BaseModel):
    datetime: str
    title: str
    text: str
