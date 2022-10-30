from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database,  models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog
from fastapi.responses import FileResponse

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


get_db = database.get_db


@router.get('/',response_model=List[schemas.ShowBlog])
def all_blogs(db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/post', status_code=201)
def create_blog(request: schemas.Blog, db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(request, db)


@router.get('//{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id :int,db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request: schemas.Blog, db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(id, db)
   



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id : int, db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)

@router.post('/generate')
def generate_certificate():
    return blog.generate_certificate()

@router.get('/download_xlfile')
def download_xlfile():
    return FileResponse("Test.xlsx",media_type="application/xls", filename='download.xlsx')


