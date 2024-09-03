from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=50), unique=True, index=True)
    hashed_password = Column(String(length=255), nullable=False)
    blogs = relationship("Blog", back_populates="author")
    likes = relationship("Like", back_populates="user")
    comments = relationship("Comment", back_populates="author")

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), index=True)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="blogs")
    likes = relationship("Like", back_populates="blog")
    comments = relationship("Comment", back_populates="blog")

class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, index=True)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    blog = relationship("Blog", back_populates="likes")
    user = relationship("User", back_populates="likes")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    blog = relationship("Blog", back_populates="comments")
    author = relationship("User", back_populates="comments")
