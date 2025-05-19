from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from web.fastapi_demo.src.auth.schemas import User_Token

auth_router = APIRouter(tags=['user authentication'])

@auth_router.post("/auth/verify", response_class=JSONResponse)
def verifytoken(token: User_Token):
    return {
        "auth_res": "OK"
    }