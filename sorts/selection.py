#acha o menor número e o coloca na primeira posição
#O(n^2)
def selection_sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range (i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

lista = [11,9,66,30,12,2,8,1,77,125,200]

print(selection_sort(lista))