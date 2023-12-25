from pydantic import BaseModel, EmailStr, Field


class Item(BaseModel):
    id = int
    name: str = Field(min_length=3, title='Name', default='Unnamed')
    price: float = Field(gt=0, title='Prise', default=0.0)
    description: str = Field(default='Описание отсутствует', title='Description')


class User(BaseModel):
    id: int
    firstname: str = Field(min_length=3, title='Firstname')
    lastname: str = Field(min_length=3, title='Lastname')
    email: EmailStr
    password: str = Field(min_length=4)


class User_In(BaseModel):
    firstname: str = Field(min_length=3, title='Firstname')
    lastname: str = Field(min_length=3, title='Lastname')
    email: EmailStr
    password: str = Field(min_length=4)


class Order(BaseModel):
    id = int
    item = Item
    user = User



