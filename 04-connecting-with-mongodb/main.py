from fastapi import FastAPI, HTTPException
from typing import List

from database import collection
from models import User

app = FastAPI()

@app.get("/")
async def hello():
    return {"Message":"Hello world"}

@app.post("/users/", response_model=User)
async def create_user(user: User):
    new_user = await collection.insert_one(user.dict())
    created_user = await collection.find_one({"_id": new_user.inserted_id})
    return created_user

@app.get("/users/", response_model=List[User])
async def list_users():
    users = await collection.find().to_list(1000)
    return users

@app.get("/users/{id}", response_model=User)
async def get_user(id: str):
    user = await collection.find_one({"_id": id})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")
