def karatsubaMultiplication(x, y):
    
    if len(str(x)) == 1 and len(str(y)) == 1:
        return x * y

    n = max(len(str(x)),len(str(y))) // 2
    
    a = x // 10 ** n 
    b = x %  10 ** n
    c = y // 10 ** n 
    d = y %  10 ** n
    
    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    ad_bc = karatsubaMultiplication(a+b, c+d) - ac - bd
    
    ans = (10 ** (2*n) ) * ac + (10 ** n) * ad_bc + bd
    
    return ans

if __name__ == "__main__":
    print(karatsubaMultiplication(5678, 1234))
    
