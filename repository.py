from sqlalchemy.orm import Session
import entity
import models
import schema


class Repository:
    def __init__(self, database: Session):
        self.database = database

    def login(self, login: entity.Login):
        user = self.database.query(models.User).filter(models.User.username == login.username, models.User.password == login.password).first()

        return user