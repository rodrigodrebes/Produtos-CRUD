import json
import pytest
from aplicacao import app, db
from aplicacao.modelos import Produto

@pytest.fixture(scope='function')
def client(app, db_setup):
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def db_setup(app):
    with app.app_context():
        db.create_all()
    yield
    with app.app_context():
        db.drop_all()

def test_adicionar_produto(client):
    novo_produto = {"nome": "Produto Teste", "categoria": "Categoria Teste", "preco": 100.0}
    response = client.post("/produtos", json=novo_produto)
    assert response.status_code == 201
    assert b"Produto adicionado" in response.data

# Restante dos testes

def test_obter_produto(client):
    produto = Produto(nome="Teste", categoria="Categoria teste", preco=10.0)
    with app.app_context():
        db.session.add(produto)
        db.session.commit()
        produto_id = produto.id
    response = client.get(f'/produtos/{produto_id}')
    assert response.status_code == 200
    assert b"Teste" in response.data

# Demais testes
