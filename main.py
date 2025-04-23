# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel
# app = FastAPI()

# @app.get("/")
# def index():
#     return {'data': {'name': "Patryk"}}

# @app.get("/blog")
# def blog(limit : int, published : bool = True, sort: Optional[str] = None):
#     return {'data': f'{limit} and {published}, {sort} blog posts'}




# class Blog(BaseModel):
#     title: str
#     body: str
#     published: Optional[bool]

# @app.post("/post")
# def creatre_blog(blog: Blog):
#     return {'data': blog.title}








# @app.get("/blog/123")
# def blog():
#     return {'data': 'blog'}

# @app.get("/blog/{id}")
# def blog(id: int):
#     return {'data': id}



# @app.get("/blog/{id}/comments")
# def comments(id: int):
#     return {'data': {id: 'comments'}}

