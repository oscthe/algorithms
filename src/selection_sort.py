


def selection_sort(A):    
    for i in range(len(A)):
        min_index = i
        for j in range(i+1, len(A)):
            if A[min_index] > A[j]:
                min_index = j
                
        A[i], A[min_index] = A[min_index], A[i]
 