from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

import repository
import cat_repository
import database
import entity
import schema
import models


app = FastAPI()

def get_repository():
    return repository.Repository(database.Session())

def get_repository_cat():
    return cat_repository.Repository(database.Session())

@app.post("/auth/login")
async def login(user: schema.Login, repository: repository.Repository = Depends(get_repository)):
    login = repository.login(entity.Login(username=user.username, password=user.password))

    print(login)
    if login is None:
        raise HTTPException(status_code=422, detail="Usuário inválido")

    return ('Usuário logado!')

@app.post("/cats")
async def create(cat: schema.Cat, repository: cat_repository.Repository = Depends(get_repository_cat)):
    cat_ent = repository.create(entity.Cat(name=cat.name, age=cat.age, color=cat.color))
    cat_show = schema.Show(id=cat_ent.id, name=cat_ent.name, age=cat_ent.age, color=cat_ent.color)
    return cat_show

@app.get("/cats")
async def get_all(repository: cat_repository.Repository = Depends(get_repository_cat)):
    list_cats = []
    for item in repository.get_all():
        list_cats.append(schema.Show(
            name=item.name,
            age=item.age,
            color=item.color
        ))
    return list_cats

@app.get("/{cat_id}")
async def get_cat_by_id(cat_id: int, repository: cat_repository.Repository = Depends(get_repository_cat)):
    cat = repository.find_by_id(cat_id)
    if cat is None:
        raise HTTPException(status_code=404, detail="Cadastro não encontrado")
    cat_schema = schema.Show(id=cat.id, name=cat.name, age=cat.age, color=cat.color)
    return cat_schema

@app.delete("/{cat_id}")
async def cat_delete(cat_id: int, repository: cat_repository.Repository = Depends(get_repository_cat)):
    cat = repository.find_by_id(cat_id)
    if cat is None:
        raise HTTPException(status_code=404, detail="Cadastro não encontrado")
    repository.cat_delete(cat.id)
    return "Cadastro removido com sucesso!"

@app.patch("/{cat_id}")
async def cat_update(cat_id: int, new_cat: schema.Cat_Update, repository: cat_repository.Repository = Depends(get_repository_cat)):
    cat = repository.find_by_id(cat_id)
    if cat is None:
        raise HTTPException(status_code=404, detail="Cadastro não encontrado")
    cat_new = repository.cat_update(cat.id, new_cat.dict(exclude_unset=True))
    return "Cadastro atualizado com sucesso"



