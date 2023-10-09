from fastapi import FastAPI
import json
import request

app = FastAPI()

from fastapi.middleware.cors import (
     CORSMiddleware
)
# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/create", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# - endpoint que retorna 5 filmes recomendados da semana (definidos em uma lista no python)
@app.get("/filmes/top5melhoresSemana")
def getTop5melhoresSemana():
    json = request.getTop5TrendingMovies()
    filmes = []
    for filme in json:
        filmes.append(filme['original_title'])
    
    return filmes

@app.get("/filmes/getMovieInfo")
def getMovieInfo():
    json = request.getMovieInfo()
    
    return json

@app.get("/filmes/getMovieByNameAndSortByPopular/{name}")
def getMovieByNameAndSortByPopular(name: str):
    json = request.getMovieByNameAndSortByPopular(name)
    
    return json

@app.get("/atores/getFilmesAtor/{id}")
def getFilmesAtor(id: int):
    json = request.getMoviesFromPeople(id)
    return json

@app.get("/atores/{id}")
def getAtor(id: str):
    json = request.getPeopleByIdJson(id)
    return json