# Testes FastAPI

- uvicorn aula14_adicionando_marca:app --reload
    - POST
        
        [http://127.0.0.1:8000/api/produtos/](http://127.0.0.1:8000/api/produtos/)
        
        1. Criar produto com marca válida
            - Já feito e no arquivo produtos_14.json:
                
                [http://127.0.0.1:8000/api/produtos/61/](http://127.0.0.1:8000/api/produtos/61/)
                
                ```json
                {"nome": "Monitor Ultra", "preco": 1200.0, "marca": "Dell"}
                ```
                
                ```json
                {
                    "id": 61,
                    "nome": "Monitor Ultra",
                    "preco": 1200,
                    "marca": "Dell"
                  }
                ```
                
        2. Criar com marca ausente
            
            ```json
            {"nome": "Monitor Ultra", "preco": 1200.0}
            ```
            
            Saída esperada: 400 Bad Request (`detail.marca` indica campo obrigatório)
            
        3. Criar com marca vazia/curta
            
            ```json
            {"nome": "Monitor", "preco": 1000.0, "marca": " "}
            ```
            
            Saída esperada: 400 Bad Request (`detail.marca` indica erro de validação)
            
    - PUT
        1. Atualizar marca via PUT
            - Já feito e no arquivo produtos_14.json:
                
                [http://127.0.0.1:8000/api/produtos/1/](http://127.0.0.1:8000/api/produtos/1/)
                
                ```json
                {"nome": "Notebook Pro", "preco": 3800.0, "marca": "Lenovo"}
                ```
                
                ```json
                {
                    "id": 1,
                    "nome": "Notebook Pro",
                    "preco": 3800,
                    "marca": "Lenovo"
                  }
                ```
                
    - GET
        1. Filtrar por marca existente
            
            [http://127.0.0.1:8000/api/produtos/?marca=Dell](http://127.0.0.1:8000/api/produtos/?marca=Dell)
            
        2. Filtrar por marca inexistente
            
            [http://127.0.0.1:8000/api/produtos/?marca=MarcaFantasma](http://127.0.0.1:8000/api/produtos/?marca=MarcaFantasma)
            
        3. Combinar marca e preço
            
            [http://127.0.0.1:8000/api/produtos/?marca=Dell&preco_minimo=2000](http://127.0.0.1:8000/api/produtos/?marca=Dell&preco_minimo=2000)
            
        4. Ordenação crescente por marca
            
            [http://127.0.0.1:8000/api/produtos/?ordering=marca](http://127.0.0.1:8000/api/produtos/?ordering=marca)
            
        5. Ordenação decrescente por marca
            
            [http://127.0.0.1:8000/api/produtos/?ordering=-marca](http://127.0.0.1:8000/api/produtos/?ordering=-marca)
            
        6. Busca textual pela marca
            
            [http://127.0.0.1:8000/api/produtos/?search=dell](http://127.0.0.1:8000/api/produtos/?search=dell)
            
        7. Busca sem resultados
            
            [http://127.0.0.1:8000/api/produtos/?search=termoinexistente](http://127.0.0.1:8000/api/produtos/?search=termoinexistente)

- uvicorn aula15_adicionando_estoque:app --reload
    - POST
        1. Criar com estoque válido - Já criado 
            
            [http://127.0.0.1:8000/api/produtos/62/](http://127.0.0.1:8000/api/produtos/62/)
            
        2. Criar com estoque zero - Já criado
            
            [http://127.0.0.1:8000/api/produtos/63/](http://127.0.0.1:8000/api/produtos/63/)
            
        3. Criar com estoque negativo
            
            ```json
            {"nome": "Fone", "preco": 150.0, "marca": "Sony", "estoque": -5}
            ```
            
            saída esperada: 400 Bad Request (`detail.estoque` avisa que não pode ser negativo)
            
        4. Criar com tipo inválido
            
            ```json
            {"nome": "Fone", "preco": 150.0, "marca": "Sony", "estoque": "muitos"}
            ```
            
            saída esperada: 400 Bad Request (`detail.estoque` avisa que deve ser inteiro)
            
        - GET
            1. Filtrar por estoque mínimo
            
            [http://127.0.0.1:8000/api/produtos/?estoque_minimo=10](http://127.0.0.1:8000/api/produtos/?estoque_minimo=10)
            
            1. Filtrar por estoque máximo
                
                [http://127.0.0.1:8000/api/produtos/?estoque_maximo=5](http://127.0.0.1:8000/api/produtos/?estoque_maximo=5)
                
            2. Filtrar por faixa de estoque
                
                [http://127.0.0.1:8000/api/produtos/?estoque_minimo=10&estoque_maximo=30](http://127.0.0.1:8000/api/produtos/?estoque_minimo=10&estoque_maximo=30)
                
            3. Ordenar crescente por estoque
                
                [http://127.0.0.1:8000/api/produtos/?ordering=estoque](http://127.0.0.1:8000/api/produtos/?ordering=estoque)
                
            4. Ordenar decrescente por estoque
                
                [http://127.0.0.1:8000/api/produtos/?ordering=-estoque](http://127.0.0.1:8000/api/produtos/?ordering=-estoque)
                
            5. Combinar marca, preço e estoque
                
                [http://127.0.0.1:8000/api/produtos/?marca=Dell&preco_minimo=1000&estoque_minimo=1](http://127.0.0.1:8000/api/produtos/?marca=Dell&preco_minimo=1000&estoque_minimo=1)