from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(req: schemas.BlogBase,db: Session):
    new_blog = models.Blog(title=req.title, body=req.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_one(id,db: Session,):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found"
        )
    return blog


def delete_blog(id,db: Session,):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found"
        )
    db.delete(blog)
    db.commit()
    return f"post {id} deleted"

def update_blog(id,req: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with {id} not found"
        )
    blog.title = req.title
    blog.body = req.body
    db.commit()
    db.refresh(blog)
    return {"message": f"blog {id} updated"}