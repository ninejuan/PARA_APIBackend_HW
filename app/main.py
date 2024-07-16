from fastapi import FastAPI
from routers import hCatRouter, sriMealRouter, userRouter
import database


app = FastAPI()
db = database.createConnection()

# /routes 경로에 대해 라우터 포함
app.include_router(hCatRouter, prefix="/hcat")
app.include_router(sriMealRouter, prefix="/srimeal")
app.include_router(userRouter, prefix="/user")

