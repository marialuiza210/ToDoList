#teste
from fastapi import FastAPI

app = FastAPI()


@app.get("/") #rota para testar a api
def read_root():
    return {"menssagem": "API do ToDo List rodando"}

