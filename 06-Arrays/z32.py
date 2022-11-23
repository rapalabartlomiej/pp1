def f(a):
    strinnn = ""
    for i in range (0,len(a)):
        strinnn = strinnn + str(a[i])+", "
    
    return strinnn
print(f([4,2,8,4,7,9,5]))