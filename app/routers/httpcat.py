from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

hCatRouter = APIRouter()

@hCatRouter.get("/")
async def get_http_cat():
    return {"message": "HTTP Cat"}