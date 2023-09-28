from fastapi import FastAPI


from user import User

app = FastAPI()
users = []


@app.get('/')
async def root():
    return users


@app.post('/registration/')
async def registration(user: User):
    users.append(user)
    return user

