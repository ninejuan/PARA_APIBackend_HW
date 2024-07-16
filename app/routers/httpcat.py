from fastapi import APIRouter, FastAPI, Header, HTTPException, Response
from pydantic import BaseModel
from typing import Optional
import requests

hCatRouter = APIRouter()

@hCatRouter.get("/")
async def get_http_cat(code: int = 200):
    response = requests.get(f'https://http.cat/{code}')
    if response.status_code == 200:
        return Response(content=response.content, media_type='image/jpeg')
    else:
        return Response(content=f"사진 받기에 실패했습니다. Status code: {response.status_code}", media_type="text/plain")