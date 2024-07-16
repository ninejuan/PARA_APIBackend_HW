from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

sriMealRouter = APIRouter()

@sriMealRouter.get("/")
async def get_sunrin_meal():
    return {"message": "Sunrin Meal"}