import database
import sqlalchemy.orm
from database import Base
from sqlalchemy import Column, Integer, String


class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), unique=True, nullable=False)

class Cat(database.Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    color = Column(String(50))

database.Base.metadata.create_all(bind=database.engine)