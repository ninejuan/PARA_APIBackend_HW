from fastapi import APIRouter, FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
import database

db = database.db
sriMealRouter = APIRouter()

@sriMealRouter.get("/")
async def get_sunrin_meal():
    return {"message": "Sunrin Meal"}