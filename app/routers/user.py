from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

userRouter = APIRouter()

@userRouter.get("/")
async def get_user():
    return {"message": "User"}