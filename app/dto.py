from pydantic import BaseModel


# Defining the schema for the request
class TextCreate(BaseModel):
    datetime: str
    title: str
    text: str
