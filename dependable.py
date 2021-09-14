from fastapi import Depends, FastAPI, HTTPException
from fastapi.param_functions import Header, Query

from typing import Optional
import logging


My_Format = '%(asctime)s %(levelname)s:%(message)s'

logging.basicConfig(
    filename='logger.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format=My_Format,
    datefmt='%d.%m.%Y %H:%M:%S'
)


async def common_parameters(q: Optional[str] = None):
    default = {'message': 'This is a message'}
    if q:
        default.update({'q': q})
    return default


async def common_users(q: Optional[str] = Query(None, max_length=5)):
    if q:
        return {'message': f'Hello {q.capitalize()}'}
    return {'message': 'This user not alowed'}


async def verify_token(x_token: str = Header(...)):
    if not x_token == 'fake_token':
        logging.debug('Somebody try accept with uncorect xtoken')
        raise HTTPException(status_code=400, detail='Token is not corect')
    logging.debug('Successfully enter in site')


app = FastAPI(dependencies=[Depends(verify_token)])


@app.get('/items/')
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get('/users/', dependencies=[Depends(verify_token)])
async def read_users(commons: dict = Depends(common_users)):
    logging.debug('Input')
    return commons
