from array import array


def f(x):
    max = x[0]
    min = x[0]
    for i in range(0,len(x)):
        if x[i]>max:
            max = x[i]
        if x[i]<min:
            min = x[i]
    return f"{max} {min}"
array = [15, 8, -31, 47, -2, 19]
print(f(array))