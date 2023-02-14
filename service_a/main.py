from fastapi import FastAPI

from model.model import User

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user/{user_id}")
async def user(user_id):
    return {"message": f"Hello {user_id}"}

@app.post("/user")
async def create_user(user: User):
    return {"message": f"Hello {user.username}"}