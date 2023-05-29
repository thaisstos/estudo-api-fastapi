from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str

class Cat(BaseModel):
    name: str
    age: int
    color: str