from sqlalchemy.orm import Session
import entity
import models
import schema


class Repository:
    def __init__(self, database: Session):
        self.database = database

    def create(self, cat: entity.Cat):
        db_cat = models.Cat(name=cat.name, age=cat.age, color=cat.color)
        self.database.add(db_cat)
        self.database.commit()
        self.database.refresh(db_cat)

        return db_cat

    def get_all(self):
        results = self.database.query(models.Cat).all()
        list_cat = []
        for item in results:
            list_cat.append(entity.Cat(
                name=item.name,
                age=item.age,
                color=item.color
            ))
        return list_cat

    def find_by_id(self, cat_id: int):
        return self.database.query(models.Cat).filter_by(id=cat_id).first()

    def cat_delete(self, cat_id: int):
        # self.database.delete(cat)
        self.database.query(models.Cat).filter_by(id=cat_id).delete()
        self.database.commit()

    def cat_update(self, cat_id: int, new_cat: dict):
        self.database.query(models.Cat).filter_by(id=cat_id).update(new_cat)
        self.database.commit()

