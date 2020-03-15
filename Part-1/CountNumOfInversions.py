def CountNumOfInversions(A):
    if len(A) == 1:
        return 0
    
    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]
    
    ctr = 0
    ctr += CountNumOfInversions(L)
    ctr += CountNumOfInversions(R)
    
    i = j = k = 0
        
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            ctr += len(L) - i
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
        
    return ctr        
        

if __name__ == "__main__":
    A = [5,4,3,2,1]
    print("List :" , A)
    print("Number of inversions" , CountNumOfInversions(A))
    
    
