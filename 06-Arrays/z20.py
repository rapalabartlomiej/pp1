def wypisz(a):
    a = int(a)
    print(f"{a}: ",end="")
    for i in range(0,a):
        print("*",end="")
    print("")
tab = [12, 6, 4, 9, 10]
for i in range(0,len(tab)):
    wypisz(tab[i])