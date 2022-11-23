tab = [8,2,5,1,9]
print(f"Array: ",end="")
for i in range(0,len(tab)):
    print(f"{tab[i]} ",end = "")
print("")
for i in range(0,len(tab)):
    tab[i]=tab[i]*tab[i]

print(f"2nd power: ",end="")
for i in range(0,len(tab)):
    print(f"{tab[i]} ",end = "")
print("")