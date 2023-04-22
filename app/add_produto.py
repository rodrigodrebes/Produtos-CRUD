
from aplicacao import app, db
from aplicacao.modelos import Produto

def criar_produto(nome, categoria, preco):
    novo_produto = Produto(nome=nome, categoria=categoria, preco=preco)
    db.session.add(novo_produto)
    db.session.commit()
    return novo_produto.id

def main():
    produtos = [
        ("Produto1", "Categoria1", 10.0),
        ("Produto2", "Categoria2", 20.0),
        ("Produto3", "Categoria3", 30.0),
    ]

    for produto in produtos:
        produto_id = criar_produto(*produto)
        print(f"Produto {produto[0]} adicionado com o ID {produto_id}")

if __name__ == "__main__":
    with app.app_context():
        main()
