import os
from sqlalchemy import Column, ForeignKey, Integer, String, Text, TIMESTAMP, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    password_hash = Column(String(20), nullable=False)
    profile_picture = Column(String(255))
    created_at = Column(TIMESTAMP)  

class Post(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    content_url = Column(String(255))
    post_description = Column(String(150))
    created_at = Column(TIMESTAMP)  
    user = relationship("User")

class Comment(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.post_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP)  
    post = relationship("Post")
    user = relationship("User")

class Like(Base):
    __tablename__ = 'likes'
    like_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.post_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    created_at = Column(TIMESTAMP)  
    post = relationship("Post")
    user = relationship("User")

class Follow(Base):
    __tablename__ = 'follows'
    follower_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    followee_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    created_at = Column(TIMESTAMP) 
    __table_args__ = (
        PrimaryKeyConstraint('follower_id', 'followee_id'),
    )
    follower = relationship("User", foreign_keys=[follower_id])
    followee = relationship("User", foreign_keys=[followee_id])

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
