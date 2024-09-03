from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserLogin):
    db_user = models.User(username=user.username, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, username: str = None, user_id: int = None):
    if username:
        return db.query(models.User).filter(models.User.username == username).first()
    if user_id:
        return db.query(models.User).filter(models.User.id == user_id).first()

def create_blog(db: Session, blog: schemas.BlogCreate, user_id: int):
    db_blog = models.Blog(**blog.dict(), author_id=user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def like_blog(db: Session, blog_id: int, user_id: int):
    db_like = models.Like(blog_id=blog_id, user_id=user_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

def comment_blog(db: Session, comment: schemas.CommentCreate, user_id: int):
    db_comment = models.Comment(**comment.dict(), author_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
    
def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.Blog(title=blog.title, content=blog.content)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog
