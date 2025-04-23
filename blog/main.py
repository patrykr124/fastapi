
from fastapi import FastAPI
from blog.routers import login
from . import  models
from .database import engine
from .routers import blog, user

app = FastAPI()

#------create connection to db--------------
models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(blog.router)
app.include_router(login.router)



    
  



