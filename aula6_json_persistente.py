import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

ARQUIVO_JSON = "produtos.json"
app = FastAPI()


# -------------------------------
# Modelos
# -------------------------------
class Item(BaseModel):
    id: int
    nome: str
    preco: float


class ItemInput(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome não pode ser vazio")
    preco: float = Field(..., gt=0, description="Preço deve ser maior que zero")


class ItemInputResponse(BaseModel):
    message: str
    dados: Item


# -------------------------------
# Funções utilitárias
# -------------------------------
def carregar_produtos() -> list[Item]:
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Item(**produto) for produto in data]
    except FileNotFoundError:
        return []


def salvar_produtos(produtos: list[Item]):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump([produto.model_dump() for produto in produtos], f, indent=2, ensure_ascii=False)


items = carregar_produtos()


# -------------------------------
# Rotas
# -------------------------------
@app.get("/produtos", response_model=list[Item])
def listar_produtos(
    min_preco: float | None = None,
    max_preco: float | None = None,
    pagina: int = 0,
    por_pagina: int = 10,
    ordenar_por: str = "id",
    ordem: str = "asc",
):
    resultado = items

    if min_preco is not None:
        resultado = [item for item in resultado if item.preco >= min_preco]
    if max_preco is not None:
        resultado = [item for item in resultado if item.preco <= max_preco]

    resultado.sort(key=lambda x: getattr(x, ordenar_por), reverse=(ordem == "desc"))

    return resultado[pagina * por_pagina : (pagina + 1) * por_pagina]


@app.get("/produtos/{item_id}", response_model=Item)
def listar_produto_por_id(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Produto não encontrado")


@app.post("/produtos", response_model=ItemInputResponse)
def criar_produto(item: ItemInput):
    novo_id = max([item_existente.id for item_existente in items], default=0) + 1
    novo_item = Item(id=novo_id, **item.model_dump())
    items.append(novo_item)
    salvar_produtos(items)
    return ItemInputResponse(message="Produto criado com sucesso", dados=novo_item)


@app.put("/produtos/{item_id}", response_model=ItemInputResponse)
def atualizar_produto(item_id: int, item_atualizado: ItemInput):
    for i, item in enumerate(items):
        if item.id == item_id:
            items[i] = Item(id=item_id, **item_atualizado.model_dump())
            salvar_produtos(items)
            return ItemInputResponse(
                message="Produto atualizado com sucesso", dados=items[i]
            )
    raise HTTPException(status_code=404, detail="Produto não encontrado")


@app.delete("/produtos/{item_id}")
def remover_produto(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            removido = items.pop(i)
            salvar_produtos(items)
            return {"message": f"Produto '{removido.nome}' removido com sucesso"}
    raise HTTPException(status_code=404, detail="Produto não encontrado")


# Rodar servidor:
# uvicorn aula6_json_persistente:app --reload
# Acesse a documentação em http://localhost:8000/docs
