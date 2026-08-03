# Exemplos de FastAPI das aulas

## Visão geral

Este projeto reúne exemplos usados nas aulas para demonstrar a construção de APIs com FastAPI, evoluindo de rotas simples até operações de CRUD com persistência em JSON.

## Requisitos

- Python 3.10 ou superior
- pip

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/marrcandre/fastapi-bsi4.git
   cd fastapi-bsi4
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   No Windows, use:

   ```bash
   .venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Como executar

Cada arquivo representa um exemplo independente. Para executar, escolha um dos arquivos e inicie o Uvicorn informando o módulo e a aplicação.

Exemplo com a aula 2A:

```bash
uvicorn aula2a:app --reload
```

Para executar outro exemplo, substitua o nome do módulo:

```bash
uvicorn aula6_json_persistente:app --reload
```

Após iniciar o servidor, acesse a documentação interativa em:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Estrutura dos exemplos

- aula2a.py
- aula2b.py
- aula3a.py
- aula3b_filtros.py
- aula4_crud_completo.py
- aula5_crud_completo_validacao_filtro_ordenacao_paginacao.py
- aula6_json_persistente.py

## Dados de apoio

O arquivo produtos.json é usado pelo exemplo com persistência em JSON.
