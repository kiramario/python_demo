from enum import Enum
from fastapi import FastAPI
from fastapi import Depends, Query, Path, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from pydantic import BaseModel
from web.fastapi_demo.src.schemas import User
from web.fastapi_demo.src.auth.router import auth_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

def common_parameters(
    q: Annotated[str, Query(description="Query string", min_length=3, max_length=50)],
    item_id: Annotated[int, Path(..., title="The ID of the user to get")]
):
    return {"q": q, "item_id": item_id}

@app.get("/items/{item_id}")
async def read_item(params: Annotated[dict, Depends(common_parameters)]):
    item_id = params.get("item_id")

    if params.get("q"):
        return {"item_id":  params.get("item_id"), "q": params.get("q")}
    return {"item_id": item_id}


@app.post("/users/")
async def create_user(user: Annotated[User, Body(..., title="The user to create")]):
    return {"user": user}




app.include_router(auth_router)