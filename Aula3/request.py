import requests

url = "https://api.themoviedb.org/3/discover/movie"
params = "?include_adult=false&include_video=false&language=en-US&page=1&sort_by=vote_count.desc&primary_release_date.gte=2022-01-01"
api_key = "&api_key=5b3819951044f6aa1b37f96daf47c074"

endpoint = url + params + api_key

headers = {"accept": "application/json"}

response = requests.get(endpoint, headers=headers)

print(response.text)
