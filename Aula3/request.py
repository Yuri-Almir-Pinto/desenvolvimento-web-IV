import requests

url = "https://api.themoviedb.org/3/discover/movie"
params = "?sort_by=vote_count.desc"
api_key = "&api_key=5b3819951044f6aa1b37f96daf47c074"

endpoint = url + params + api_key

headers = {"accept": "application/json"}

response = requests.get(endpoint, headers=headers)

data = response.json()
filmes = data['results']
quantia = 0

for item in filmes:
    quantia = quantia + 1
    print("---------------------")
    print ("Nome: " + item['original_title'])
    print (f"Id: {item['id']}")

print("---------------------")
print(quantia)

# print(data['results'][0]['original_title'])
