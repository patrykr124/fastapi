from typing import List
from fastapi import Depends, status, APIRouter

from blog.oauth2 import get_current_user
from .. import schemas, database
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="",
    tags=["Blogs"],
    responses={404: {"description": "Not found"}},
)


@router.post("/blog", status_code=status.HTTP_201_CREATED, tags=["Blogs"])
def create(req: schemas.BlogBase, db: Session = Depends(database.get_db)):
    return blog.create_blog(req, db)


@router.get("/blog", tags=["Blogs"], response_model=List[schemas.BlogBase])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.get("/blog/{id}", tags=["Blogs"], response_model=schemas.BlogBase)
def get_one(id, db: Session = Depends(database.get_db)):
    return blog.get_one(id, db)


@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"])
def deletePost(id, db: Session = Depends(database.get_db)):
    return blog.delete_blog(id, db)


@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
def update_blog(id, req: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update_blog(id, req, db)
