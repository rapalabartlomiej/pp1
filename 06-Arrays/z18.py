tab = [15, 8, 31, 47, 2, 19]
print(f"Array: ",end="")
for i in range(0,len(tab)):
    print(f"{tab[i]} ",end = "")
print("")
suma = 0
for i in range(0,len(tab)):
    suma = suma + tab[i]
suma = suma / len(tab)
print(suma)