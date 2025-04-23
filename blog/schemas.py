from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title:str
    body:str
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[BlogBase] = []
    class Config:
        orm_mode = True

class Blog(BaseModel):
    creator: ShowUser
    class Config:
        orm_mode = True
    
class User(BaseModel):
    name:str
    email:str
    password:str
    
class Login(BaseModel):
    email: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

        

    

