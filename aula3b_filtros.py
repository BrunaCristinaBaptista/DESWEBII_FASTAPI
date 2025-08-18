from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# Base de dados fictícia
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500},
    {"id": 2, "nome": "Mouse", "preco": 80},
    {"id": 3, "nome": "Teclado", "preco": 150},
    {"id": 4, "nome": "Monitor", "preco": 1200},
    {"id": 5, "nome": "Impressora", "preco": 300},
]

@app.get("/produtos")
def listar_produtos(
    min_preco: Optional[float] = Query(None, description="Preço mínimo"),
    max_preco: Optional[float] = Query(None, description="Preço máximo")
):
    resultado = produtos

    if min_preco is not None:
        resultado = [p for p in resultado if p["preco"] >= min_preco]

    if max_preco is not None:
        resultado = [p for p in resultado if p["preco"] <= max_preco]

    return {"produtos": resultado}

# Para executar o código, utilize o comando:
# uvicorn aula_3b_filtros:app --reload


# Para testar, acesse as URLs:
# - http://localhost:8000/produtos
# - http://localhost:8000/produtos?min_preco=100
# - http://localhost:8000/produtos?max_preco=1000
# - http://localhost:8000/produtos?min_preco=100&max_preco=1000
