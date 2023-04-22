import os
import requests

base_url = os.getenv("BASE_URL", "http://localhost:5000")


# Testando POST para adicionar um novo produto
novo_produto = {"nome": "Produto Teste", "categoria": "Categoria Teste", "preco": 50.0}
response = requests.post(f"{base_url}/produtos", json=novo_produto)
print("POST /produtos:", response.json())

"""# Testando GET para obter um produto específico
produto_id = response.json()["id"]
response = requests.get(f"{base_url}/produtos/{produto_id}")
print(f"GET /produtos/{produto_id}:", response.json())
 """
# Testando GET para listar todos os produtos
response = requests.get(f"{base_url}/produtos")
print("GET /produtos:", response.json())

""" # Testando PUT para atualizar um produto
produto_atualizado = {"nome": "Produto Atualizado", "categoria": "Categoria Teste", "preco": 60.0}
response = requests.put(f"{base_url}/produtos/{produto_id}", json=produto_atualizado)
print(f"PUT /produtos/{produto_id}:", response.json())

# Testando DELETE para remover um produto
response = requests.delete(f"{base_url}/produtos/{produto_id}")
print(f"DELETE /produtos/{produto_id}:", response.json())

# Testando GET novamente para verificar se o produto foi removido
response = requests.get(f"{base_url}/produtos")
print("GET /produtos (após DELETE):", response.json())

# Testando DELETE para remover todos os produtos
response = requests.delete(f"{base_url}/produtos/all")
print("DELETE /produtos/all:", response.json())

# Testando GET novamente para verificar se todos os produtos foram removidos
response = requests.get(f"{base_url}/produtos")
print("GET /produtos (após DELETE ALL):", response.json())
 """