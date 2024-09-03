from pydantic import BaseModel
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class BlogCreate(BaseModel):
    title: str
    content: str

class Blog(BaseModel):
    id: int
    title: str
    content: str
    author: User

    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    content: str
    blog_id: int

class Comment(BaseModel):
    id: int
    content: str
    blog: Blog
    author: User

    class Config:
        orm_mode = True

class Like(BaseModel):
    blog_id: int
    user_id: int

    class Config:
        orm_mode = True

