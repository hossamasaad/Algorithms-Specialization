def MergeSort(A):
    if len(A) > 1:
        
        mid = len(A) // 2                       # mid of the list
        L = A[:mid]                             # first half of the list
        R = A[mid:]                             # second half of the list
        
        MergeSort(L)                            # Sort first half
        MergeSort(R)                            # Sort second half
        
        # Merge two halfs L,R to the main list A
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
        

if __name__ == "__main__":
    A = [1,2,7,5,6,2,-1,0,4]
    print("List before sorting:" , A)
    MergeSort(A)
    print("List after sorting:" , A)

    
