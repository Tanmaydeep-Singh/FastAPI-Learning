from fastapi import APIRouter, HTTPException, status, Depends, Header
from pydantic import BaseModel
from typing import Dict, Union
from utils import hash_password, verify_password
from database import collection  # Ensure this is correctly imported and connected
from datetime import datetime, timedelta
from jose import JWTError, jwt as jose_jwt

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

class AuthCredentials(BaseModel):
    email: str
    password: str

@router.post('/login')
async def authenticate_user(credentials: AuthCredentials):
    user = await collection.find_one({"email": credentials.email})
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if not verify_password(credentials.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    # Create JWT token
    access_token = create_access_token(email=user["email"], id=str(user["_id"]))
    return {"access_token": access_token, "token_type": "bearer"}

SECRET = "MYLITTLESECRET"
ALGO = "HS256"

def create_access_token(email: str, id: str, expires_delta: Union[timedelta, None] = None) -> str:
    to_encode = {
        'sub': email,
        'id': id
    }
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=1)  # Default expiration time if not provided
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jose_jwt.encode(to_encode, SECRET, algorithm=ALGO)
    return encoded_jwt

def get_current_user(authorization: str = Header(None)) -> Dict[str, str]:
    if authorization is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing")

    token = authorization.split("Bearer ")[-1]
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token missing")

    try:
        payload = jose_jwt.decode(token, SECRET, algorithms=[ALGO])
        email = payload.get('sub')
        user_id = payload.get('id')
        if email is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

        user = collection.find_one({"email": email, "_id": user_id})
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

@router.get("/me", response_model=UserResponse)
async def get_me(current_user: Dict[str, str] = Depends(get_current_user)):
    return {
        "name": current_user["name"],
        "email": current_user["email"]
    }

@router.get("/token")
async def get_token():
    return {"Message": "Hello"}
