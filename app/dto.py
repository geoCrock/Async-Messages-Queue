from pydantic import BaseModel


# Определяем схему для запроса и ответа
class TextCreate(BaseModel):
    title: str
    text: str
