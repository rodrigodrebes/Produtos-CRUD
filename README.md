CRUD de Produtos em Python

Este é um projeto simples de CRUD (Criar, Ler, Atualizar, Excluir) para gerenciar produtos, implementado usando Python, Flask, SQLAlchemy e Sqlite.


<b>OBJETIVOS</b> 

O principal objetivo deste projeto é fornecer um sistema de gerenciamento de produtos que permite aos usuários adicionar, atualizar, recuperar e excluir produtos através de uma API RESTful.


<b>FUNCIONALIDADES</b> 

Adicionar um novo produto
Atualizar um produto existente
Recuperar um produto por ID
Recuperar todos os produtos
Excluir um produto por ID



<b> ESTRUTURA </b> 

O projeto está estruturado da seguinte forma:


app/aplicacao/:

__init__.py: Inicializa a aplicação e importa as rotas.

config.py: Contém a configuração da aplicação.

modelos.py: Contém a classe Produto, que representa um produto e fornece métodos para gerenciar dados.

rotas.py: Contém as rotas da API e as funções que lidam com as requisições HTTP.


app/testes/:

__init__.py: Arquivo vazio para identificar o diretório como um pacote Python.

conftest.py: Contém as configurações para os testes, como a criação do cliente de teste do Flask.

test_app_pytest.py: Contém testes unitários para a aplicação, usando pytest.

test_requests.py: Contém testes de integração para a aplicação, usando a biblioteca requests.


app/:

add_produto.py: Script para adicionar um produto de exemplo ao banco de dados.

createdatabase.py: Script para criar o banco de dados e as tabelas necessárias.

executar.py: Script para executar a aplicação.





<b>UTILIZAÇÃO </b> 


Instale as dependências necessárias usando pip


Crie o banco de dados e as tabelas necessárias executando o script createdatabase.py:

python createdatabase.py

Execute a aplicação usando o script executar.py:

python executar.py

Use um cliente HTTP ou um navegador web para interagir com a API.

Execute os testes:

Testes unitários:

pytest app/testes/test_app.py

Testes de integração:

python app/testes/test_requests.py
