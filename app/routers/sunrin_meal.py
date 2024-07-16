from fastapi import APIRouter, FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
import requests

sriMealRouter = APIRouter()

# Sunrin Meal NPI EndPoint
# https://npi.ny64.kr/snt_lunch?month=<월>&day=<일>

@sriMealRouter.get("/")
async def get_sunrin_meal(month: int = 3, day: int = 5):  
    response = requests.get(f"https://npi.ny64.kr/snt_lunch?month={month}&day={day}").json()
    meals = response["data"][0]
    return {
        "code": 200,
        "date": meals['date'],
        "meals": meals["menu"]
    }