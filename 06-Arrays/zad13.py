def f(x):
    suma = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j]%2==0:
                suma +=x[i][j]
    return suma




array = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
print(f(array))