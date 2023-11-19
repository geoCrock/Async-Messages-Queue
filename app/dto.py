from pydantic import BaseModel


# Определяем схему для запроса и ответа
class TextCreate(BaseModel):
    title: str
    text: str

# class TextResponse(BaseModel):
#     id: int
#     created_at: datetime
#     title: str
#     text: str
