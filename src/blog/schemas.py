from pydantic import BaseModel

class Message(BaseModel):
    message: str

class Articles(BaseModel):
    id: int
    title: str
    data: str