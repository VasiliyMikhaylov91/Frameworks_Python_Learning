from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI
from werkzeug.security import generate_password_hash
from models import Item, User, User_In, Order

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("Firstname", sqlalchemy.String(32)),
    sqlalchemy.Column("Lastname", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("Password", sqlalchemy.String(64))
)

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("price", sqlalchemy.Float),
    sqlalchemy.Column("description", sqlalchemy.Text)
)

orders = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("item", sqlalchemy.ForeignKey("items.id")),
    sqlalchemy.Column("user", sqlalchemy.ForeignKey("users.id"))
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/users/", response_model=User)
async def create_user(user: User_In):
    query = users.insert().values(Firstname=user.firstname,
                                  Lastname=user.firstname,
                                  email=user.email,
                                  password=generate_password_hash(user.password))
    query = users.insert().values(user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)
