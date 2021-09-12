from fastapi import FastAPI, Query, Form, HTTPException
from typing import Optional, List
from pydantic import BaseModel


app = FastAPI()


user_names = ['root', 'admin', 'administrator']


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post('/items/')
async def create_item(item: Item):
    return item


@app.get('/items/')
async def read_items(q: Optional[str] = Query(None, max_length=5)):
    results = {'items': [{'item_id': "Foo"}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


@app.get('/new_items/')
async def get_new_items(q: List[str] = Query(['foo', 'bar'])):
    query_items = q
    return query_items


@app.post('/login/')
async def login(username: str = Form(...), password: str = Form(...)):
    if username not in user_names:
        return HTTPException(status_code=404, detail=f"{username} not alowed ")
    return {'username': username}
