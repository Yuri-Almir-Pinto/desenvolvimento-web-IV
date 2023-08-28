import requests

URL_MOVIES = "https://api.themoviedb.org/3/discover/movie"
URL_GENRES = "https://api.themoviedb.org/3/genre/movie/list?language=en"
PARAMS_POPULAR = "?sort_by=vote_count.desc"
API_KEY = "5b3819951044f6aa1b37f96daf47c074"

def getPopularsJson(): # Retorna um json com os filmes mais populares
    endpoint = URL_MOVIES + PARAMS_POPULAR + "&api_key=" + API_KEY
    headers = {"accept": "application/json"}
    response = requests.get(endpoint, headers=headers)

    return response.json()

def getGenresJson(): # Retorna uma lista com todos os ids e seus nomes.
    genresEndpoint = URL_GENRES + "&api_key=" + API_KEY
    headers = {"accept": "application/json"}
    response = requests.get(genresEndpoint, headers=headers)

    return response.json()

def findGenre(generos_filme, generos): # Recebe uma lista de id de gêneros, e a lista de gêneros existentes, 
    # e retorna o nome de cada gênero como uma lista.
    Lista_generos = []
    for generoF in generos_filme:
        for genero in generos:
            if generoF == genero['id']:
                Lista_generos.append(genero['name'])
    return Lista_generos

def getMovieInfo():
    filmes = getPopularsJson()['results']
    generos = getGenresJson()['genres']
    quantia = 0
    for item in filmes:
        quantia = quantia + 1
        print("---------------------")
        print ("Nome: " + item['original_title'])
        print (f"Id: {item['id']}")
        print (f"Gêneros: {findGenre(item['genre_ids'], generos)}")

    print("---------------------")
    print(quantia)

if __name__ == "__main__":
    getMovieInfo()
