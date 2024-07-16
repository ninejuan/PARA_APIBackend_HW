# main.py
from fastapi import FastAPI
from routers.httpcat import hCatRouter
from routers.sunrin_meal import sriMealRouter
from routers.user import userRouter
from database import *

app = FastAPI()
db = createConnection()

# /routes 경로에 대해 라우터 포함
app.include_router(hCatRouter, prefix="/hcat")
app.include_router(sriMealRouter, prefix="/srimeal")
app.include_router(userRouter, prefix="/user")

