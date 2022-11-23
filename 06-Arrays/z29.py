a=[1,0,9,6,4.25]
b = input("podaj liczbe: ")
b = float(b)
for i in range(0,len(a)):
    if a[i]>b:
        print(f"{a[i]} ",end="")