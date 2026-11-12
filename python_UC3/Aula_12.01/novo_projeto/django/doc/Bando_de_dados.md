# Documentação dos arquivos 
## Tabela: Categoria

Campos:
- nome 
    - Charfield(20)
- categoria 
    - Charfield(50)


## Tabela: Produtos

Campos:
- nome 
    - Charfield(20)
- categoria
    - Charfield(50)
- descricao
    - Textfield(200)
- preco
    - intergerChoices
- Qtd 
    - intergerChoices
- Descricao 
    - Textfield(200)


## Tabela: Cliente

Campos:
- perfil estendido 
    - Charfield(200)
- registo
    - 
- sexo 
    - Charfield(200)
- nome social
    - Charfield(200)
- foto de perfil
    - imagefield 
- telefone
    - Charfield
- data de nascimento
    - Charfield 
- cpf unico 
    - Charfield 

## Tabela: Endereco/Entrega 

Campos:
- cadastro de endereco 
    - Charfield 
- relaciomanto de cliente e enderecos 
    - manytomanufield
- enderecos de entrega 
    - manytomanyfield

## Tabela: Pedido 

Campos:
- detalhes do pedido 
    - textfield
- status do pedido
    - charfield
- preco total do pedido
    - intergefield

## Tabela: Itens do pedido 

Campos:
- detalhes do itens no carrinho 
    - textfield(max_length=200)
- registro de qtd com preco fixo sem alteracoes 
    - textfield(max_length=200)

## Tabela: Comentarios e avaliações 

Campos:
- comentario
    - textfield(max_length=200)
- avaliacao 
    - textfield(max_length=200)