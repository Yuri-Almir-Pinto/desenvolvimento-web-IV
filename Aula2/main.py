from fastapi import FastAPI
from datetime import datetime, timedelta

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

@app.get("/horarios/{cidade}")
def horarios(cidade):
    if cidade == "Tokyo":
        return {
            "Cidade": cidade,
            "Hora": datetime.now() + timedelta(hours=12)
        }
    if cidade == "Brasilia":
        return {
            "Cidade": cidade,
            "Hora": datetime.now()
        }
    if cidade == "Londres":
        return {
            "Cidade": cidade,
            "Hora": datetime.now() + timedelta(hours=4)
        }

# uvicorn main:app --reload