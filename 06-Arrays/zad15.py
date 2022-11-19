from array import array


def f(x):
    for i in range(len(x)):
        x[i][i] = 1
    return x

def pokaz(x):
    for i in range(len(x)):
        print(x[i])
array = [[0,0,0],[0,0,0],[0,0,0]]
array = f(array)
pokaz(array)