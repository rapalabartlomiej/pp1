def f(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j]:
                x[i][j] = False
            else: 
                x[i][j] = True
    return x
array = [[True,False],[True,True],[False,False]]
print(f(array))