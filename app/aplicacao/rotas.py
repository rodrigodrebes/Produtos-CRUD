from flask import request, jsonify, current_app as app
from aplicacao import db
from aplicacao.modelos import Produto

@app.route("/produtos", methods=["POST"])
def adicionar_produto():
    data = request.get_json()
    novo_produto = Produto(nome=data["nome"], categoria=data["categoria"], preco=data["preco"])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({"mensagem": "Produto adicionado", "id": novo_produto.id}), 201

@app.route("/produtos/<int:produto_id>", methods=["GET"])
def obter_produto(produto_id):
    produto = db.session.get(Produto, produto_id)
    if produto is None:
        return jsonify({"mensagem": "Produto não encontrado"}), 404
    return jsonify(produto.to_dict())

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([produto.to_dict() for produto in produtos])

@app.route("/produtos/<int:produto_id>", methods=["PUT"])
def atualizar_produto(produto_id):
    data = request.get_json()
    produto = db.session.get(Produto, produto_id)
    if produto is None:
        return jsonify({"mensagem": "Produto não encontrado"}), 404
    produto.nome = data["nome"]
    produto.categoria = data["categoria"]
    produto.preco = data["preco"]
    db.session.commit()
    return jsonify({"mensagem": "Produto atualizado"})

@app.route("/produtos/<int:produto_id>", methods=["DELETE"])
def remover_produto(produto_id):
    produto = db.session.get(Produto, produto_id)
    if produto is None:
        return jsonify({"mensagem": "Produto não encontrado"}), 404
    db.session.delete(produto)
    db.session.commit()
    return "", 204

@app.route("/produtos", methods=["DELETE"])
def remover_todos_produtos():
    produtos = Produto.query.all()
    for produto in produtos:
        db.session.delete(produto)
    db.session.commit()
    return jsonify({"mensagem": "Todos os produtos foram removidos"})
