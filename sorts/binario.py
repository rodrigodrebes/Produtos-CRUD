def binary_search(sequence, item):
    index_inicial = 0
    index_final = len(sequence) -1

    while index_inicial <= index_final:
        meio = index_inicial + (index_final)