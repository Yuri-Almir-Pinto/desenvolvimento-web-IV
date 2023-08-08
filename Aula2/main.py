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

# uvicorn main:app --reload