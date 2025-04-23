from typing import List
from fastapi import Depends, APIRouter
from blog.repository import user

from .. import schemas, database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.post("/user", tags=["User"])
def create_user(req: schemas.User, db: Session = Depends(database.get_db)):
    return user.create_user(req, db)


@router.get("/alluser", response_model=List[schemas.ShowUser], tags=["User"])
def all_user(db: Session = Depends(database.get_db)):
    return user.get_all_user(db)


@router.get("/user/{id}", response_model=schemas.ShowUser, tags=["User"])
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get_user(db, id)
