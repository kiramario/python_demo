#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.main
# @Calendar: 2025-04-21 11:28
# @Time: 11:28
# @Author: mammon, kiramario
import datetime
from enum import Enum
from fastapi import FastAPI
from fastapi import Depends, Query, Path, Body
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

"""

"""

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {"message": "Hello World"}

"""
/items/{item_id parameters
"""
def common_parameters(
    q: Annotated[str, Query(description="Query string", min_length=3, max_length=50)] = "default",
    item_id: Annotated[int, Path(..., title="The ID of the user to get")] = 0
):
    return {"q": q, "item_id": item_id}

@app.get("/items/{item_id}")
async def read_item(params: Annotated[dict, Depends(common_parameters)]):
    item_id = params.get("item_id")

    if params.get("q"):
        return {"item_id":  params.get("item_id"), "q": params.get("q")}
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

class User(BaseModel):
    name: str
    age: int

@app.post("/users/")
async def create_user(user: Annotated[User, Body(..., title="The user to create")]):
    return {"user": user}


def run():
    pass


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
