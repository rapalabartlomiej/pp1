tab = [15, 8, 31, 47, 2, 19]
print(f"Array: ",end="")

#for i in range(0,len(tab)):
#    print(f"{tab[i]} ",end = "")
insa = 0
while insa !=len(tab):
    print(f"{tab[insa]} ",end = "")
    insa = insa +1

print("")
suma = 0

insa = 0
while insa !=len(tab):
     suma = suma + tab[insa]
     insa = insa +1

suma = suma / len(tab)
print(suma)