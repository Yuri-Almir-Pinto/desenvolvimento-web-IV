from fastapi import FastAPI
import json
import request

app = FastAPI()

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