#O(n^2)

def bubble (lista):
    for i in range(0, len(lista) -1):
        for j in range(0, len(lista) -1 -i):
            if lista[j] > lista[j+1]:
                lista[j], lista [j+1] = lista[j+1], lista[j]
    return lista

l = [1,80,45,9,3,2,66,12,120]
letra = ["n", "b", "a", "w", "c", "s", "r", "u", "d", "k"]

print(bubble(l))
print(bubble(letra))