from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo para POST
class Item(BaseModel):
    nome: str
    preco: float

# Rota GET
@app.get("/produtos")
def listar_produtos():
    return [
    {"id": 1, "nome": "Notebook", "preco": 3500},
    {"id": 2, "nome": "Mouse", "preco": 80},
    {"id": 3, "nome": "Teclado", "preco": 150},
    {"id": 4, "nome": "Monitor", "preco": 1200},
    {"id": 5, "nome": "Impressora", "preco": 300},
    ]

# Rota POST
@app.post("/produtos")
def criar_produto(item: Item):
    return {"mensagem": "Produto criado com sucesso", "dados": item}

# Rodar servidor:
# uvicorn main:app --reload