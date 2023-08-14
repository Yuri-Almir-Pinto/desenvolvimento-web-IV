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

@app.get("/ehpar/{numero}") // Atividade 1
def ehpar(numero: int):
    if numero % 2 == 0:
        return {
            "result": True 
        }
    return {
        "result": False
    }

@app.get("/horarios/{cidade}") // Atividade 2
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

@app.get("/dia") // Atividade 3
def dia():
    dia = datetime.now().weekday()
    if dia == 0:
        dia = "Segunda-feira"
    elif dia == 1:
        dia = "Terça-feira"
    elif dia == 2:
        dia = "Quarta-feira"
    elif dia == 3:
        dia = "Quinta-feira"
    elif dia == 4:
        dia = "Sexta-feira"
    elif dia == 5:
        dia = "Sábado"
    elif dia == 6:
        dia = "Domingo"
    return {
        "dia": dia
    }

# uvicorn main:app --reload