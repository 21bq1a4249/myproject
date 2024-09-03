from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class BlogCreate(BaseModel):
    title: str
    content: str

class Blog(BaseModel):
    id: int
    title: str
    content: str
    author: User

    class Config:
        from_attributes = True

class CommentCreate(BaseModel):
    content: str
    blog_id: int

class Comment(BaseModel):
    id: int
    content: str
    blog: Blog
    author: User

    class Config:
        from_attributes = True

class Like(BaseModel):
    blog_id: int
    user_id: int

    class Config:
        from_attributes = True
        
class BlogCreate(BaseModel):
    title: str
    content: str
