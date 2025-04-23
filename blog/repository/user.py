from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.hashing import Hash


def create_user(req: schemas.User, db: Session):
    Hash.hash_user(req.password)
    new_user = models.User(
        name=req.name, email=req.email, password=Hash.hash_user(req.password)
    )
    if not new_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User not created"
        )
    existing_user = db.query(models.User).filter(models.User.email == req.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"user": new_user, "message": "User created"}

def get_all_user(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found"
        )
    return user