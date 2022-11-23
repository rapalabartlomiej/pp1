tab = [15, 8, 31, 47, 2, 19]
print(f"existed array: ",end="")
for i in range(0,len(tab)):
    print(f"{tab[i]} ",end = "")
print("")

print(f"reverse array: ", end="")
for i in range(1,len(tab)+1):
    print(f"{tab[len(tab)-i]} ",end = "")