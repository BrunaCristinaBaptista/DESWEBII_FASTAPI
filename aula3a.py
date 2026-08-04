from typing import Optional

from fastapi import FastAPI

app = FastAPI()

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500},
    {"id": 2, "nome": "Mouse", "preco": 120},
    {"id": 3, "nome": "Teclado", "preco": 250},
]

@app.get("/produtos/{id_produto}")
def get_produto(id_produto: int):
    for produto in produtos:
        if produto["id"] == id_produto:
            return produto
    return {"erro": "Produto não encontrado"}

@app.get("/produtos")
def listar_produtos(categoria: Optional[str] = None):
    # Como ainda não temos banco, o filtro é apenas ilustrativo
    return produtos

# Para rodar o servidor, use o comando:
# uvicorn aula3:app --reload

# Exemplos de uso:
# - Obter um produto específico: GET /produtos/1
# - Filtrar produtos por categoria: GET /produtos?categoria=eletronicos
