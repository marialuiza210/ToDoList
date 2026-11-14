# teste
from fastapi import FastAPI, HTTPException
from database import client

app = FastAPI()


@app.get("/")  # rota para testar a api
async def health_check():
    try:
        #tenta enviar um 'ping' ao banco de dados
        await client.admin.command('ping')
        return {
            "status": "ok",
            "menssagem": "API ToDoList rodando",
            "bd": "conectado com sucesso"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"erro na ligação com o banco: {str(e)}")
