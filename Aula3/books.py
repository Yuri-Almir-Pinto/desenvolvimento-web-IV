from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/book/id/{id}")
def getBookId(id: int):
    with open("books.json") as j:
        data = json.load(j)
        for item in data:
            if item['id'] == id:
                return item
        return {"error": f"book {id} not found"}

@app.get("/book/year/{year}")
def getBookYear(year: int):
    with open("books.json") as j:
        jsons = []
        data = json.load(j)
        for item in data:
            if item['year'] == year:
                jsons.append(item)

        if len(jsons) != 0:
            return jsons
        else:
            return {"error": f"no books from {year}"}

@app.get("/book/title/{title}")
def getBookYear(title: str):
    with open("books.json") as j:
        jsons = []
        data = json.load(j)
        for item in data:
            if title in item['title']:
                jsons.append(item)

        if len(jsons) != 0:
            return jsons
        else:
            return {"error": f"no books named '{title}'"}

@app.get("/book/author/{author}")
def getBookYear(author: str):
    with open("booksv2.json") as j:
        jsons = []
        data = json.load(j)
        for item in data:
            for a in item['authors']:
                if author in a:
                    jsons.append(item)

        if len(jsons) != 0:
            return jsons
        else:
            return {"error": f"no books from {author}"}