from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(50),unique=True, index = True, nullable=False)
    email = Column(String(255),unique=True, nullable=False)
    hashed_password = Column(String(255),nullable = False)
    role = Column(String(20),default="user")
    tasks = relationship("Task",back_populates="owner")

class Task(Base):
    __tablename__="tasks"
    id = Column(Integer,primary_key=True,index = True)
    title = Column(String(100),nullable = False)
    description = Column(String(500),nullable=True)
    completed = Column(Boolean,default=False)
    priority = Column(String(20),default = "medium")
    created_at = Column(DateTime,default=datetime.utcnow)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User",back_populates="tasks")


