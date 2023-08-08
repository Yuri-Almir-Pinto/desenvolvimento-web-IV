from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/hora")
def horacerta():
    print("batata")
    return {
        "Hora": datetime.now(),
        "Local": "BR"
    }

@app.get("/upper/{nome}")
def upper(nome):
    return {
        "nome": nome,
        "upper": nome.upper()
    }

@app.get("/ehpar/{numero}")
def ehpar(numero: int):
    if numero % 2 == 0:
        return {
            "result": True 
        }
    return {
        "result": False
    }

# uvicorn main:app --reload