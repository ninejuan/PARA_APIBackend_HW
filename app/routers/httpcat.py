from fastapi import APIRouter, FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

@hCatRouter.get("/")
async def get_http_cat(code: int = 200):
    return {"message": "HTTP Cat"}