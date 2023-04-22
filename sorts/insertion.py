#O(n^2)

def insertion_sort(A):
    for i in range(1,len(A)):
        j = i-1
        while A[j] > A[j+1] and j>= 0:
            A[j], A[j+1] = A[j+1], A[j]
            j-=1
    return A

list = [11,14,20,2,3,6,88,9,78,41]

print(insertion_sort(list))
