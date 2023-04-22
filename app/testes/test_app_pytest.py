import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from aplicacao.modelos import Produto
from aplicacao import db
import json
from flask import url_for, current_app as app
from aplicacao.modelos import Produto
from conftests import test_app, test_db, test_client

def adicionar_produto_teste(test_client):
    data = {
        "nome": "Produto Teste",
        "categoria": "Teste",
        "preco": 50.0
    }
    return test_client.post("/produtos", data=json.dumps(data), content_type="application/json")

def test_adicionar_produto(test_client):
    data = {
        "nome": "Produto Teste",
        "categoria": "Teste",
        "preco": 50.0
    }
    response = test_client.post("/produtos", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 201
    assert "id" in response.json

def test_atualizar_produto(test_client):
    response = adicionar_produto_teste(test_client)
    produto_id = response.json["id"]

    data = {
        "nome": "Produto Atualizado",
        "categoria": "Atualizado",
        "preco": 60.0
    }
    response = test_client.put(f"/produtos/{produto_id}", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 200
    assert "mensagem" in response.json

def test_obter_produto(test_client):
    response = adicionar_produto_teste(test_client)
    produto_id = response.json["id"]

    response = test_client.get(f"/produtos/{produto_id}")
    assert response.status_code == 200
    assert "Produto Teste" in response.get_data(as_text=True)

def test_remover_produto(test_client):
    response = adicionar_produto_teste(test_client)
    produto_id = response.json["id"]

    response = test_client.delete(f"/produtos/{produto_id}")
    assert response.status_code == 204

def test_listar_produtos(test_client):
    response = test_client.get("/produtos")
    assert response.status_code == 200

def test_produto_nao_encontrado(test_client):
    response = test_client.get("/produtos/100")
    assert response.status_code == 404


#python -m pytest test_app_pytest.py