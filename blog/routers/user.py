from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database,  models, oauth2
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)


get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request : schemas.User, db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return user.create_user(request, db)
    


@router.get('/{id}', response_model= schemas.ShowUser)
def get_user(id: int, db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return user.get_user(id, db)