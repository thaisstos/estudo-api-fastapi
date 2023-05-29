from pydantic import BaseModel
from typing import Optional


class Login(BaseModel):
    username: str
    password: str

class Cat(BaseModel):
    name: str
    age: int
    color: str

class Show(BaseModel):
    id: int
    name: str
    age: int
    color: str

class Cat_Update(BaseModel):
    name: Optional[str]
    age: Optional[int]
    color: Optional[str]
