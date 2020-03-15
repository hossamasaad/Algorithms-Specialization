
def quickSort(A):
    n = len(A)
    if n < 1:
        return A
    
    pivot = A.pop()                     # Take last element as Pivot 
    L,R = [], []
    for e in A:
        if e > pivot:
            R.append(e)
        else:
            L.append(e)

    
    return quickSort(L) + [pivot] + quickSort(R)

if __name__ == "__main__":
    A = [5,4,3,2,1]
    print("List before sorting :" , A)
    A = quickSort(A)
    print("List after sorting :" , A)
    
    
