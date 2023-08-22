import requests

api_key = "5b3819951044f6aa1b37f96daf47c074"

url = "https://api.themoviedb.org/3/discover/movie"
endpoint = f"{url}?include_adult=false&include_video=false&language=en-US&page=1&sort_by=vote_count.desc&api_key={api_key}&primary_release_date.gte=2022-01-01"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
