from os import name
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    item_dict['name'] = item_dict['name'].capitalize()
    if item.tax:
        item_dict.update({'price_with_tax': item.price * item.tax})
    return item_dict


@app.put('/items/{item_id}/')
async def put_item(item_id: int, item: Item):
    item_dict = item.dict()
    item_dict['name'] = item_dict['name'].capitalize()
    if item.tax:
        item_dict.update({'price_with_tax': item.price * item.tax})
    return {'item_id': item_id, **item_dict}


@app.get('/items/')
async def read_items(
        q: Optional[str] = Query(
            None, title='just name', max_length=5, description="for test"
            )
        ):
    result = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        result.update({'q': q})
    return result
