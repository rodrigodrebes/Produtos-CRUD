import unittest
import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aplicacao import app, db
from aplicacao.modelos import Produto

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_adicionar_produto(self):
        novo_produto = {"nome": "Produto Teste", "categoria": "Categoria Teste", "preco": 100.0}
        response = self.client.post("/produtos", json=novo_produto)
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Produto adicionado", response.data)

    # Restante dos testes descomentados

    def test_obter_produto(self):
        produto = Produto(nome="Teste", categoria="Categoria teste", preco=10.0)
        with app.app_context():
            db.session.add(produto)
            db.session.commit()
            produto_id = produto.id
        response = self.client.get(f'/produtos/{produto_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Teste", response.data)

    def test_atualizar_produto(self):
        produto = Produto(nome="Teste", categoria="Categoria teste", preco=10.0)
        with app.app_context():
            db.session.add(produto)
            db.session.commit()
            produto_id = produto.id
        response = self.client.put(f'/produtos/{produto_id}', json=dict(nome="Novo nome", categoria="Nova categoria", preco=20.0))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Produto atualizado", response.data)

    def test_remover_produto(self):
        produto = Produto(nome="Teste", categoria="Categoria teste", preco=10.0)
        with app.app_context():
            db.session.add(produto)
            db.session.commit()
            produto_id = produto.id
        response = self.client.delete(f'/produtos/{produto_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Produto removido", response.data)

    def test_listar_produtos(self):
        produto = Produto(nome="Teste", categoria="Categoria teste", preco=10.0)
        with app.app_context():
            db.session.add(produto)
            db.session.commit()
        response = self.client.get('/produtos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"nome", response.data)

    def test_produto_nao_encontrado(self):
        response = self.client.get('/produtos/9999')
        self.assertEqual(response.status_code, 404)
        response_json = json.loads(response.data)
        self.assertEqual(response_json['mensagem'], "Produto não encontrado")

if __name__ == "__main__":
    unittest.main()






""" Os testes neste arquivo não afetam o banco de dados principal nem os arquivos do projeto. Eles usam um banco de dados em memória (in-memory) para realizar os testes. Isso é feito configurando o SQLAlchemy com a URI 'sqlite:///:memory:' no método setUp.
Com isso, todos os testes são executados em um banco de dados temporário que existe apenas na memória enquanto os testes são executados. Quando os testes são concluídos, o banco de dados em memória é descartado e não afeta o banco de dados principal ou persistido.

Além disso, o método setUp é chamado antes de cada teste, criando um novo banco de dados em memória, e o método tearDown é chamado após cada teste, removendo o banco de dados em memória. Isso garante que cada teste seja executado isoladamente e não afete os outros testes ou o banco de dados principal. """