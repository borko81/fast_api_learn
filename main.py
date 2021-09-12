from enum import Enum
from fastapi import FastAPI
from typing import Optional


app = FastAPI()


class ModelName(str, Enum):
    first = 'f_name'
    second = 'l_name'


@app.get('/')
async def root():
    return {'message': 'This is a message'}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {'item': item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.first:
        return {'model_name': model_name, 'message': ModelName.first}
    if model_name == ModelName.second:
        return {'model_name': model_name, 'message': ModelName.second}


@app.get('files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}


@app.get('/names/{item_id}')
async def read_items(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
