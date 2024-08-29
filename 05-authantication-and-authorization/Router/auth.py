from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Union
from utils import hash_password
from database import collection  # Ensure this is correctly imported and connected

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    name: str
    email: str

class CreateUserResponse(BaseModel):
    message: str
    user: UserResponse

@router.post('/auth', response_model=CreateUserResponse)
async def create_user(user: UserCreate):
    # Check if the user already exists
    existing_user = await collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Hash the password
    hashed_password = hash_password(user.password)

    # Create a new user in the database
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }
    result = await collection.insert_one(new_user)

    # Retrieve the created user
    created_user = await collection.find_one({"_id": result.inserted_id})

    # Debug print statement
    print("created_user", created_user)

    if created_user:
        return {
            "message": "User created successfully",
            "user": {
                "name": created_user["name"],
                "email": created_user["email"]
            }
        }
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="User creation failed")
