def f (x,n):
    
    n = n-1
    if n != 0:
        return x*f (x,n)
    else:
        return x
    
print(f(5,4))