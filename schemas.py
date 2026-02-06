from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True
