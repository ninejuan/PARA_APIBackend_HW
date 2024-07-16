from fastapi import APIRouter, FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
import database

db = database.db
userRouter = APIRouter()

@userRouter.get("/")
async def get_user():
    return {"message": "User"}


"""
/signup
method: POST
header: {
    id: str,
    passwd: str
}

response: {
    status: int,
    message: str
}
"""
@userRouter.post("/signup")
def signup(id: str = Header(None), passwd: str = Header(None)):
    # id, pw가 None인 경우 400 에러 반환
    if id is None or passwd is None:
        raise HTTPException(status_code=400, detail="id or pw is None")
    
    # 입력한 id가 이미 db에 있다면 400 에러 반환
    if db['users'].find_one({"id": id}):
        raise HTTPException(status_code=400, detail="id already exists")
        
    # db에 사용자 추가
    db['users'].insert_one({"id": id, "pw": passwd})
    
    return {'status': 200, 'message': 'success'}
    

"""
/signin
method: POST
header: {
    id: str,
    passwd: str
}

response: {
    status: int,
    message: str
}
"""
@userRouter.post("/signin")
def signin(id: str = Header(None), passwd: str = Header(None)):
    if id is None or passwd is None:
        raise HTTPException(status_code=400, detail="id or pw is None")

    if db['users'].find_one({"id": id, "pw": passwd}):
        return {'status': 200, 'message': 'success'}
    else:
        raise HTTPException(status_code=400, detail="id or pw is wrong")

"""
/check
method: GET
header: {
    id: str,
    passwd: str
}

response: {
    status: int,
    message: str
}
"""
@userRouter.get("/check")
def check(id: str = Header(None), passwd: str = Header(None)):
    if db['users'].find_one({"id": id, "pw": passwd}):
        return {'status': 200, 'message': 'success'}
    else:
        raise HTTPException(status_code=400, detail="id or pw is wrong")

"""
/leave
method: DELETE
header: {
    id: str,
    passwd: str
}

response: {
    status: int,
    message: str
}
"""
@userRouter.get("/leave")
def check(id: str = Header(None), passwd: str = Header(None)):
    if db['users'].find_one({"id": id, "pw": passwd}):
        try:
            db["users"].delete_one({"id": id, "pw": passwd})
            return {'status': 200, 'message': 'success'}
        except:
            return {'status': 400, 'message': 'failed'}
    else:
        raise HTTPException(status_code=400, detail="id or pw is wrong")