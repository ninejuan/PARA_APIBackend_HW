from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from main import db

userRouter = APIRouter()