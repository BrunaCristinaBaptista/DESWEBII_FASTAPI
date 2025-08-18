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
        {"id": 1, "nome": "Mouse", "preco": 89.90},
        {"id": 2, "nome": "Teclado", "preco": 199.90}
    ]

# Rota POST
@app.post("/produtos")
def criar_produto(item: Item):
    return {"mensagem": "Produto criado com sucesso", "dados": item}

# Rodar servidor:
# uvicorn main:app --reload