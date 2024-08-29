from fastapi import FastAPI
from Router import auth

app = FastAPI()

app.include_router(router=auth.router)

@app.get('/')
async def hello():
    return {"Message": "Hello"}