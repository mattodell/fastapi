# main.py

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/me")
async def read_user_me():
    return {"iser_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
