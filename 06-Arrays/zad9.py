def f(x):
    dlugoscmax=0
    miejsce = 0
    for i in range(0,len(x)):
        if len(x[i])>dlugoscmax:
            dlugoscmax = len(x[i])
            miejsce = i

    return x[miejsce]

array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
print(f(array))