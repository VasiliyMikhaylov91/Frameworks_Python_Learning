from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: str = None


class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: EmailStr
    password: str


class Order(BaseModel):
    items: List[Item]
    user: User
