from typing import List
from .database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
     __tablename__ = "blogs"
     id: Mapped[int] = mapped_column(primary_key=True)
     title: Mapped[str]
     body: Mapped[str]
     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
     creator: Mapped[["User"]] = relationship("User", back_populates="blogs")
     
class User(Base):
     __tablename__ = 'user'
     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str]
     email: Mapped[str]
     password: Mapped[str]
     blogs: Mapped[List["Blog"]] = relationship("Blog", back_populates="creator")
     
     