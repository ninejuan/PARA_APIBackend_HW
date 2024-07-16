from fastapi import APIRouter, FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
import database

db = database.db
hCatRouter = APIRouter()

@hCatRouter.get("/")
async def get_http_cat():
    return {"message": "HTTP Cat"}