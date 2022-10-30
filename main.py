from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit = 10, published : bool = True, sort: Optional[str] = None):
    if published:
        return {'data':f'{limit} from the published blog'}
    else:
        return {'data':f'{limit} blog from db'}

   
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {"data": id }


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blog')
def create_blog(blog : Blog):
    return {'data':f'Blog is created with the title as {blog.title} '}