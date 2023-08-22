import requests

url = "https://api.themoviedb.org/3/discover/movie"
params = "?sort_by=vote_count.desc"
api_key = "&api_key=5b3819951044f6aa1b37f96daf47c074"
genresEndpoint = "https://api.themoviedb.org/3/genre/movie/list?language=en"

endpoint = url + params + api_key
genresEndpoint = genresEndpoint + api_key

headers = {"accept": "application/json"}

response = requests.get(endpoint, headers=headers)
response2 = requests.get(genresEndpoint, headers=headers)

data = response.json()
data2 = response2.json()
filmes = data['results']
generos = data2['genres']
quantia = 0

def findGenre(generos_filme):
    Lista_generos = []
    for generoF in generos_filme:
        for genero in generos:
            if generoF == genero['id']:
                Lista_generos.append(genero['name'])
    return Lista_generos

for item in filmes:
    quantia = quantia + 1
    print("---------------------")
    print ("Nome: " + item['original_title'])
    print (f"Id: {item['id']}")
    print (f"Gêneros: {findGenre(item['genre_ids'])}")

print("---------------------")
print(quantia)

# print(data['results'][0]['original_title'])
                